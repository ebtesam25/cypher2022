from dataclasses import field
import time
import random
import logging
from argparse import ArgumentParser, RawTextHelpFormatter
import csv

import psycopg2
from psycopg2.errors import SerializationFailure

def create_users(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, email VARCHAR(200), userpassword VARCHAR(30), phone VARCHAR(20), name VARCHAR(30))"
        )
        cur.execute("UPSERT INTO users (id, email, userpassword, phone, name) VALUES (1, 'jon@fisherman.com', 'password1', '12524568877', 'jon stewart'), (2, 'joe@gmail.com', 'password1', '15685558989', 'joe someone')")
        logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    print ("users table created")


def add_users(conn, uname, pw, uphone, uemail):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM users")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        
        cur.execute("UPSERT INTO users (id, email, userpassword, phone, name) VALUES (" + i +", '" + uemail + "', '" + pw + "', '" + uphone +"', '" + uname +"')")
        logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    print ("user added")


def login(conn, uemail, pw):
    with conn.cursor() as cur:
        cur.execute("SELECT id, email, userpassword, phone, name FROM users")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        for row in rows:
            print(row)
            print (type(row))
            if row[1] == uemail and row[2] == pw:
                print ("found")
                return True, row[3], row[4]
        return False, 'none', 'none'

def delete_users(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM defaultdb.users")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    with conn.cursor() as cur:
        cur.execute("DROP TABLE users")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()

    print ("users table deleted")


def connector():
    # conn=psycopg2.connect("dbname='nifty-puma-91.defaultdb' user='muntaser' password='passtheword' host='free-tier.gcp-us-central1.cockroachlabs.cloud' port='26257'")
    conn=psycopg2.connect("dbname='immigrace-cypher-916.defaultdb' user='muntaser' password='geturownpassword' host='free-tier14.aws-us-east-1.cockroachlabs.cloud' port='26257'")
    return conn


def initialize(conn):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS questions (id INT PRIMARY KEY, question VARCHAR(800), answer VARCHAR(1200))"
        )
        # cur.execute("UPSERT INTO users (id, email, userpassword, usertype, name) VALUES (1, 'jon@fisherman.com', 'password1', 'fisherman', 'jon stewart'), (2, 'joe@gmail.com', 'password1', 'customer', 'joe someone')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    print ("table created")    


def addq(question, answer, conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM questions")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        i = 1
        for row in rows:
            i = i + 1
        i = str(i)
        
        cur.execute("UPSERT INTO questions (id, question, answer) VALUES (" + i +", '" + question + "', '" + answer + "')")
        # logging.debug("create_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    print ("question added")    


def getallquestions(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id, question, answer FROM questions")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        results = []
        for row in rows:
            q = {}
            print(row)
            # print (type(row))
            q['id'] = str(row[0])
            q['question'] = str(row[1])
            q['question'] = str(row[2])

            results.append(q)

        return results    



def getresources(conn, types):
    # ress = []
    with conn.cursor() as cur:
        cur.execute("SELECT resourcename, tags FROM cdata")
        # logging.debug("print_balances(): status message: %s", cur.statusmessage)
        rows = cur.fetchall()
        conn.commit()
        # print(f"Balances at {time.asctime()}:")
        results = []
        for row in rows:
            q = {}
            print(row)
            # print (type(row))
            q['name'] = str(row[0])
            q['tags'] = str(row[1])
            tag = str(row[1])
            tag = tag.lower()
            # q['question'] = str(row[1])
            # q['question'] = str(row[2])
            
            if 'all' in types:
                results.append(str(row[0]))
                results.append("the following resources are available")
                continue
            
            tags = tag.split(';')
            if 'scholarship' in tag and 'scholarship' in types:
                results.append("the following scholarship resources are available")
            if 'legal' in tag and 'legal' in types:
                results.append("the following legal resources are available")
            if 'financial' in tag and 'financial' in types:
                results.append("the following financial resources are available")
                                
            print (tags)
            for t in tags:
                if 'scholarship' in t and 'scholarship' in types:
                   results.append(str(row[0]))
                   break
                if 'legal' in t and 'legal' in types:
                   results.append(str(row[0]))
                   break
                if 'financial' in t and 'financial' in types:
                   results.append(str(row[0]))
                   break
                   
        return results
                




def purgedb(conn):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM defaultdb.questions")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    with conn.cursor() as cur:
        cur.execute("DROP TABLE questions")
        logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    conn.commit()
    
    # with conn.cursor() as cur:
    #     cur.execute("DELETE FROM defaultdb.cdata")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()
    # with conn.cursor() as cur:
    #     cur.execute("DROP TABLE cdata")
    #     logging.debug("delete_accounts(): status message: %s", cur.statusmessage)
    # conn.commit()

    print ("cdata table deleted")


def importfromcsv(conn, csvfile, fieldlist):
    cdstring = "CREATE TABLE IF NOT EXISTS cdata (cid INT GENERATED ALWAYS AS IDENTITY" 
    #, first_name VARCHAR(50), last_name VARCHAR(50), dob DATE, email VARCHAR(255), PRIMARY KEY (cid))"
    
    for f in fieldlist:
        cdstring += ", " + f['name'] + " " + f['type'] + "(" +f['size'] + ")"

    cdstring += ", PRIMARY KEY (cid))"
    
    print (cdstring)
    
    with conn.cursor() as cur:
        cur.execute(cdstring)
    conn.commit()
    
    cdstring = "COPY cdata( "
    # first_name, last_name, dob, email) FROM "+csvfile  +" DELIMITER ','CSV HEADER;"
    
    for f in fieldlist:
        cdstring += f['name'] + ", "
    
    cdstring = ")".join(cdstring.rsplit(",", 1))
    cdstring += "FROM "+csvfile  +" DELIMITER ','CSV HEADER;"
    
    print (cdstring)
    
    
    # with conn.cursor() as cur:
    #     f = open(csvfile, 'r')
    #     cur.copy_from(f, "cdata", sep=',')
    #     f.close()
    #     # cur.execute(cdstring)
    
    cur = conn.cursor()
    # with open(csvfile, 'r') as f:
    #     # Notice that we don't need the `csv` module.
    #     next(f) # Skip the header row.
    #     cur.copy_from(f, 'cdata', sep=',')

    # conn.commit()
    
    with open(csvfile, 'r') as f:
        reader = csv.reader(f)
        next(reader) # Skip the header row.
        for row in reader:
            cdstring = "UPSERT INTO cdata (id, category, resourcename, link, description, eligibility, tags, contactinfo, coordinates, metadata1, metadata2) VALUES ("
            print (row)
            for r in row:
                print(r)
                print(type(r))
                cdstring +="'" + r + "',"
                
            cdstring = ")".join(cdstring.rsplit(",", 1))
                
            print (cdstring)
            cur.execute(cdstring)    
            # cur.execute("INSERT INTO cdata VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],))
            
            
    conn.commit()
    
    print("csv imported")
    




# fieldlist = []
# f = {}
# f['name'] = 'id'
# f['type'] = 'VARCHAR'
# f['size'] = '10'
# fieldlist.append(f)

# f = {}
# f['name'] = 'category'
# f['type'] = 'VARCHAR'
# f['size'] = '40'
# fieldlist.append(f)

# f = {}
# f['name'] = 'resourcename'
# f['type'] = 'VARCHAR'
# f['size'] = '100'
# fieldlist.append(f)

# f = {}
# f['name'] = 'link'
# f['type'] = 'VARCHAR'
# f['size'] = '300'
# fieldlist.append(f)

# f = {}
# f['name'] = 'description'
# f['type'] = 'VARCHAR'
# f['size'] = '2000'
# fieldlist.append(f)

# f = {}
# f['name'] = 'eligibility'
# f['type'] = 'VARCHAR'
# f['size'] = '100'
# fieldlist.append(f)

# f = {}
# f['name'] = 'tags'
# f['type'] = 'VARCHAR'
# f['size'] = '100'
# fieldlist.append(f)

# f = {}
# f['name'] = 'contactinfo'
# f['type'] = 'VARCHAR'
# f['size'] = '300'
# fieldlist.append(f)

# f = {}
# f['name'] = 'coordinates'
# f['type'] = 'VARCHAR'
# f['size'] = '100'
# fieldlist.append(f)

# f = {}
# f['name'] = 'metadata1'
# f['type'] = 'VARCHAR'
# f['size'] = '500'
# fieldlist.append(f)

# f = {}
# f['name'] = 'metadata2'
# f['type'] = 'VARCHAR'
# f['size'] = '800'
# fieldlist.append(f)



# conn = connector()
# initialize(conn)
# # purgedb(conn)

# addq("test question" , "test answer", conn)
# r = getallquestions(conn)

# print (r)


# importfromcsv(conn, "cypherimmi.csv", fieldlist)


# # delete_users(conn)
# purgedb(conn)

