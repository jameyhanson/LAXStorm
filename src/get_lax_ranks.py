'''
Created on Jan 6, 2017

@author: jamey

Desc: get lacrosse ranks from www.laxpower.com
      Write to high_schools
'''
import urllib.request
from pgdb import PgDb

class UrlRecord:
    def __init__(self, url, year, gender):
        self.url = url
        self.year = year
        self.gender = gender
        
    def getUrl(self):
        return self.url
    
    def getYear(self):
        return self.year
    
    def getGender(self):
        return self.gender
    
class HSRankRecord:
    def __init__(self, url, gender, year, rank, hs, state):
        self.url = url
        self.gender = gender
        self.year = year
        self.rank = rank
        self.hs = hs
        self.state = state
        
    def getUrl(self):
        return self.url
    
    def getGender(self):
        return self.gender
    
    def getYear(self):
        return self.year
    
    def getRank(self):
        return self.rank
    
    def getHS(self):
        return self.hs
    
    def getState(self):
        return self.state

def generateUrlRecords(startYear, endYear):
    # example: http://www.laxpower.com/update16/binboy/natlccr.php
    urlRecords = []
    genders = ['boy', 'grl'] 
    for year in range(startYear, endYear + 1):
        for gender in genders:
            strYear = str(year)[2:]
            url = ("http://www.laxpower.com/update" + strYear + "/bin" + gender + "/natlccr.php")
            urlRecord = UrlRecord(url, year, gender)
            urlRecords.append(urlRecord)
    return (urlRecords)   # a dictionary of {url:, year:, gender:}

def getHSRankRecords(urlRecord):
    response = urllib.request.urlopen(urlRecord.getUrl())
    
    HSRankRecords = []
    
    for line in response:
        row = str(line.rstrip())
        if row.find(".PHP") > 0:
            lax_rank = eval(row[row.find("b'")+3:row.find("<A")])
            school = (row[(row.find('.PHP">')+6):row.find("</A>")].strip()).replace("\\","")
            if school.find(',') > 0:
                school = school[:school.find(',')]
            school = school.replace("'", "''")  #PostgreSQL double ticks [''] are escapes for single ticks [']
            state = row[row.find("</A>") + 4:row.find("<span") - 12].strip()
            hsRankRecord = HSRankRecord(urlRecord.getUrl(), urlRecord.getGender(), urlRecord.getYear(), str(lax_rank), school, state)
            HSRankRecords.append(hsRankRecord)
        elif row.find("padding-bottom") > 0:
            response.close()
    return (HSRankRecords)

def getHSRankSQL(HSRankRecord, schema):    
    sql = ('INSERT INTO ' + schema + '.hs_ranks (' +
           'url, ' +
           'gender, ' +
           'year, ' +
           'rank, ' +
           'raw_hs_name, ' +
           'state) VALUES (' +
           "'" + HSRankRecord.getUrl() + "', " +
           "'" + HSRankRecord.getGender() + "', " +
           str(HSRankRecord.getYear()) + ", " +
           str(HSRankRecord.getRank()) + ", " +
           "'" + HSRankRecord.getHS() + "', " +
           "'" + HSRankRecord.getState() + "');")
    
    return sql
    
def main():   
    START_YEAR = 2003
    END_YEAR = 2016
    SCHEMA = 'lam' #change to lax for production
    NUM_SCHOOLS_PER_YEAR = 1500
        
    pgdb = PgDb(dbname='lax', user='lax', password='cloudera', host='/tmp/', port=5432)
    
    #urls = []
    urls = generateUrlRecords(START_YEAR, END_YEAR)
    
    hsRankRecords = []
    
    for urlRecord in urls:
        hsRankRecords = getHSRankRecords(urlRecord)
        
        for HSRankRecord in hsRankRecords:
            sql = getHSRankSQL(HSRankRecord, SCHEMA)
            pgdb.exec_sql(sql)
        
        print('Completed ', HSRankRecord.getGender(), ':', str(HSRankRecord.getYear()))
    
    # populate the high_schools table with high schools
    sql = ('INSERT INTO ' + SCHEMA + '.high_schools (' +
           'raw_name, ' +
           'state) ' + 
           '(SELECT DISTINCT ' +
           'raw_hs_name, ' +
           'state ' +
           'FROM ' + SCHEMA + '.hs_ranks ' +
           'WHERE rank <= ' + str(NUM_SCHOOLS_PER_YEAR) + ');')
    pgdb.exec_sql(sql)
    print('Populated ' + SCHEMA + '.high_schools')
    
    # update hs_ranks.hs_id
    sql = ('UPDATE ' + SCHEMA + '.hs_ranks AS hr ' +
           'SET hs_id = (' + 
           'SELECT hs.id ' +
           'FROM ' + SCHEMA + '.high_schools hs ' +
           'WHERE hs.raw_name = hr.raw_hs_name ' +
           'AND hs.state = hr.state);')
    pgdb.exec_sql(sql)
    print('Updated ' + SCHEMA + '.hs_ranks')
        
if __name__ == '__main__':
    main()
