'''
Created on Jan 12, 2017

@author: jamey

Desc: Write input files for heatmap display.
Usage: write_heatmap_files.py

'''
from pgdb import PgDb

def main():
    START_YEAR = 2003
    END_YEAR = 2016
    NUM_SCHOOLS = 1500
    SCHEMA = 'lam' # use 'lax' for production
    outfile_base = 'lax_rank_'
    genders = ['boy', 'grl'] 

    pgdb = PgDb(dbname='lax', user='lax', password='cloudera', host='/tmp/', port=5432)
    
    for year in range(START_YEAR, END_YEAR + 1):
        for gender in genders:
            outfile_name = outfile_base + gender + '_' + str(year) + '.tsv'
            
            sql = """SELECT
            hr.zipf_weight,
            hs.latitude, 
            hs.longitude,
            hr.rank, 
            hs.raw_name || ', ' || hs.state || ', ' || hs.country
            FROM """ + SCHEMA + """.high_sChools hs
            INNER JOIN lax.hs_ranks hr ON hs.id = hr.hs_id
            WHERE hr.gender = '""" + gender + "' " + \
            "AND hr.year = " + str(year) + \
            " AND hr.rank <= " +  str(NUM_SCHOOLS) + \
            " AND geolocated = True ORDER BY hr.rank;"
                        
            rows = pgdb.get_cursor(sql)

            with open(outfile_name, 'w') as file:
                header = 'weight\tlatitude\tlongitude\trank\ths_name\n'
                file.write(header)
                for row in rows:
                    file_line = str(row[0]) + '\t' + str(row[1]) + '\t' + str(row[2]) + '\t' + str(row[3]) + '\t' + row[4] + '\n'
                    file.write(file_line)
                    
                file.close()
                print('wrote ' + outfile_name)

    print('Successfully completed write_heatmap_files.py')

if __name__ == '__main__':
    main()