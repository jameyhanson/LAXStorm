'''
Created on Jan 6, 2017

@author: jamey

Desc: get lacrosse ranks from www.laxpower.com
'''

import urllib.request
import psycopg2

'''
From http://stackoverflow.com/questions/32978365/how-do-i-run-psycopg2-on-el-capitan-without-hitting-a-libssl-error
sudo ln -s /Library/PostgreSQL/9.6/lib/libssl.1.0.0.dylib /usr/local/lib
sudo ln -s /Library/PostgreSQL/9.6/lib/libcrypto.1.0.0.dylib /usr/local/lib
sudo ln -s /tmp/.s.PGSQL.5432 /var/pgsql_socket/
'''

def generateUrls(startYear, endYear):
    # example: http://www.laxpower.com/update16/binboy/natlccr.php
    gender = ['boy', 'grl']        
    urlList = []
    for year in range(startYear, endYear + 1):
        for gndr in gender:
            strYear = str(year)[2:]
            url = ("http://www.laxpower.com/update" + strYear + "/bin" + gndr + "/natlccr.php")
            urlDict = {'url':url, 'year': year, 'gender': gndr}
            urlList.append(urlDict)
    return (urlList)

def getHSRankRecords(urlDict):
    response = urllib.request.urlopen(urlDict['url'])
      
    for line in response:
        row = str(line.rstrip())
        if row.find(".PHP") > 0:
            #print (row)
            lax_rank = eval(row[row.find("b'")+3:row.find("<A")])
            school = (row[(row.find('.PHP">')+6):row.find("</A>")].strip()).replace("\\","")
            # replace single-quote with two single-quote for the insert
            school = school.replace("'", ",,")
            # sometimes HS is embedded in the name
            school = school.replace(" HS ", " ")
            # sometimes there is a , STATE in the name
            if school.find(',') > 0:
                school = school[:school.find(',')]
            state = row[row.find("</A>") + 4:row.find("<span") - 12].strip()
            print(
                 urlDict['url'], ' |',
                 urlDict['gender'], ' | ',
                 urlDict['year'], ' | ',
                 str(lax_rank), ' | ',
                 school, ' | ',
                 state)
            # writeHSRank(urlDict['url'], urlDict['gender'], urlDict['year'], str(lax_rank), school + " High School", state)
        elif row.find("padding-bottom") > 0:
            response.close()
    return (None)
   
def writeHSRank(url, gender, year, lax_rank, high_school, state):
    print(url, gender, year, lax_rank, high_school, state)
        #conn = psycopg2.connect("dbname='lax' user='lax' port = 5432 password='cloudera'")
    conn = psycopg2.connect(
                            dbname='lax',
                            user='lax',
                            port = 5432,
                            host='/tmp/', #added to avoid 'connections on Unix domain socket "/var/pgsql_socket/.s.PGSQL.5432"?'
                            password='cloudera')

    curr = conn.cursor()
    
    sql = (
           "INSERT INTO hs_rank (" +
           "url," +
           "gender, " +
           "year, " +
           "lax_rank, " +
           "high_school, " +
           "state) VALUES (" +
           "'" + url + "', " +
           "'" + gender + "', " +
           str(year) + ", " +
           str(lax_rank) + ", " +
           "'" + high_school + "', " +
           "'" + state + "')" )
    curr.execute(sql)
    conn.commit()
    conn.close()
   
def main():   
    START_YEAR = 2005
    END_YEAR = 2005 #2016
    
    urlList = generateUrls(START_YEAR, END_YEAR)    
    
    for urlDict in urlList:
        getHSRankRecords(urlDict)
    
if __name__ == '__main__':
    main()
