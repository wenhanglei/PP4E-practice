"""
显示表内容，格式化输出字段
"""

def showformat(recs, sept=('-' * 40)):
    print(len(recs), 'records')
    print(sept)
    for rec in recs:
        maxkey = max(len(key) for key in rec)
        for key in rec:
            print('%-*s => %s' % (maxkey, key, rec[key]))
        print(sept)

def dumpdb(cursor, table, format=True):
    if not format:
        cursor.execute('select * from ' + table)
        while True:
            rec = cursor.fetchone()
            if not rec: break
            print(rec)
    else:
        from makedicts import makedicts
        recs = makedicts(cursor, 'select * from ' + table)
        showformat(recs)

if __name__ == '__main__':
    import sys
    dbname, format, table = 'dbase1', False, 'people'
    cmdargs = sys.argv[1:]
    if '-' in cmdargs:
        format = True
        cmdargs.remove('-')
    if cmdargs: dbname = cmdargs.pop(0)
    if cmdargs: table = cmdargs[0]

    from loaddb import login
    conn, curs = login(dbname)
    dumpdb(curs, table, format)



























