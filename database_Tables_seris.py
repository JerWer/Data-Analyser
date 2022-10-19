#! python3


import sqlite3

"""
to be corrected: group should be in JVmeas! 

#list of tables:
    batch
    users
    samples
    cells
    pixelarea
    Groups
    JVmeas
    (Refdiode)
    MPPmeas
    SunsVoc

#sqlite variable type: TEXT, NULL, INTEGER, REAL, BLOB
"""

criteriaexclusionlist=['JVmeas.commentJV','JVmeas.linktorawdata','Groups.LayerStack',
                       'MPPmeas.commentmpp', 'MPPmeas.linktorawdata','SunsVoc.commentSV','SunsVoc.linktorawdata'] #cannot restrict search from those criteria

dropdowncriteria=['batch.batchname','users.user','samples.samplename','samples.DeviceType','JVmeas.MeasurementLongName',
                  'cells.cellname','cells.AllpixSeq','pixelarea.pixel_area','Groups.GroupName','JVmeas.SerialNumber',
                  'JVmeas.ScanDirect','JVmeas.MeasSetup',
                  'JVmeas.LightDark', 'JVmeas.aftermpp',
                  'MPPmeas.TrackingAlgo','MPPmeas.MeasSetup','MPPmeas.MeasurementLongName','MPPmeas.SerialNumber',
                  'MPPmeas.LightDark','SunsVoc.MeasurementLongName','SunsVoc.SerialNumber'
                  ]
                  
fromtocriteria=['JVmeas.Eff', 'JVmeas.Voc','JVmeas.Jsc', 'JVmeas.Isc','JVmeas.FF',
                'JVmeas.Vmpp', 'JVmeas.Jmpp', 'JVmeas.Pmpp','JVmeas.Roc','JVmeas.Rsc',
                'JVmeas.Delay','JVmeas.DelayShutter','JVmeas.IntegTime','JVmeas.NbPoints',
                'JVmeas.Vmin','JVmeas.Vmax','JVmeas.CurrentLimit',
                'JVmeas.IlluminationIntensity',
                'MPPmeas.TrackingDuration','MPPmeas.Vstart', 'MPPmeas.Vstep', 'MPPmeas.Delay',
                'MPPmeas.IlluminationIntensity','MPPmeas.PowerEnd','MPPmeas.PowerAvg',
                'SunsVoc.pIsc','SunsVoc.pJsc','SunsVoc.pVoc','SunsVoc.pFF','SunsVoc.pPmpp','SunsVoc.pETA',
                'SunsVoc.temperature'
                ]

timecriteria=['JVmeas.DateTimeJV', 'MPPmeas.DateTimeMPP','SunsVoc.DateTimeSunV']


def CreateAllTables(db_conn):
    
    theCursor = db_conn.cursor()

#%%    
    try: 
        theCursor.execute("""CREATE TABLE IF NOT EXISTS batch(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                batchname TEXT NOT NULL,
                users_id INTEGER,
                FOREIGN KEY(users_id) REFERENCES users(id) ON DELETE CASCADE
                );""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table batch couldn't be created")
    try: 
        theCursor.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user TEXT NOT NULL UNIQUE
                );""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table users couldn't be created")
    try:
        theCursor.execute("""CREATE TABLE IF NOT EXISTS samples(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                samplename TEXT NOT NULL,
                DeviceType TEXT,
                batch_id INTEGER,
                FOREIGN KEY(batch_id) REFERENCES batch(id) ON DELETE CASCADE
                );""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table samples couldn't be created")        
    try:
        theCursor.execute("""CREATE TABLE IF NOT EXISTS cells(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                cellname TEXT,
                AllpixSeq TEXT,
                pixelarea_id REAL,
                samples_id INTEGER,
                batch_id INTEGER,
                FOREIGN KEY(pixelarea_id) REFERENCES pixelarea(id),
                FOREIGN KEY(batch_id) REFERENCES batch(id) ON DELETE CASCADE,
                FOREIGN KEY(samples_id) REFERENCES samples(id)
                );""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table cells couldn't be created")
    try:
        theCursor.execute("""CREATE TABLE IF NOT EXISTS pixelarea(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                pixel_area REAL
                )""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table pixelarea couldn't be created")
    try:
        theCursor.execute("""CREATE TABLE IF NOT EXISTS Groups(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                GroupName TEXT,
                LayerStack TEXT
                )""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table Group couldn't be created")
    try:
        theCursor.execute("""CREATE TABLE IF NOT EXISTS JVmeas(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                DateTimeJV TEXT,
                Eff REAL,
                Voc REAL,
                Jsc REAL,
                Isc REAL,
                FF REAL,
                Vmpp REAL,
                Jmpp REAL,
                Pmpp REAL,
                Roc REAL,
                Rsc REAL,
                ScanDirect TEXT,
                Delay REAL,
                DelayShutter REAL,
                IntegTime REAL,
                Vmin REAL,
                Vmax REAL,
                MeasSetup TEXT,
                NbPoints REAL,
                CurrentLimit REAL,
                LightDark TEXT,
                IlluminationIntensity REAL,
                commentJV TEXT,
                MeasurementLongName TEXT,
                SerialNumber TEXT,
                linktorawdata TEXT,
                aftermpp INTEGER,
                Groups_id INTEGER,
                samples_id INTEGER,
                batch_id INTEGER,
                cells_id INTEGER,
                FOREIGN KEY(batch_id) REFERENCES batch(id) ON DELETE CASCADE,
                FOREIGN KEY(samples_id) REFERENCES samples(id),
                FOREIGN KEY(cells_id) REFERENCES cells(id),
                FOREIGN KEY(Groups_id) REFERENCES Groups(id)
                );""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table JVmeas couldn't be created")
    # try:
    #     theCursor.execute("""CREATE TABLE IF NOT EXISTS Refdiode(
    #             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #             IsRefDiodeMeasured INTEGER,
    #             RefDiodeNomCurr REAL,
    #             RefDiodeMeasCurr REAL,
    #             temperature REAL
    #             );""")
    #     db_conn.commit()
    # except sqlite3.OperationalError:
    #     print("Table Refdiode couldn't be created")
    try:
        theCursor.execute("""CREATE TABLE IF NOT EXISTS MPPmeas(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                DateTimeMPP TEXT,
                TrackingAlgo TEXT,
                MeasSetup TEXT,
                TrackingDuration REAL,
                Vstart REAL,
                Vstep REAL,
                Delay REAL,
                PowerEnd REAL,
                PowerAvg REAL,
                commentmpp TEXT,
                LightDark TEXT,
                IlluminationIntensity REAL,
                MeasurementLongName TEXT,
                SerialNumber TEXT,
                linktorawdata TEXT,
                samples_id INTEGER,
                batch_id INTEGER,
                cells_id INTEGER,
                FOREIGN KEY(batch_id) REFERENCES batch(id) ON DELETE CASCADE,
                FOREIGN KEY(samples_id) REFERENCES samples(id),
                FOREIGN KEY(cells_id) REFERENCES cells(id)
                );""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table MPPmeas couldn't be created")
    try:
        theCursor.execute("""CREATE TABLE IF NOT EXISTS SunsVoc(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                DateTimeSunV TEXT,
                pIsc REAL,
                pJsc REAL,
                pVoc REAL,
                pFF REAL,
                pPmpp REAL,
                pETA REAL,
                temperature REAL,
                commentSV TEXT,
                MeasurementLongName TEXT,
                SerialNumber TEXT,
                linktorawdata TEXT,
                Groups_id INTEGER,
                samples_id INTEGER,
                batch_id INTEGER,
                cells_id INTEGER,
                FOREIGN KEY(batch_id) REFERENCES batch(id) ON DELETE CASCADE,
                FOREIGN KEY(samples_id) REFERENCES samples(id),
                FOREIGN KEY(cells_id) REFERENCES cells(id),
                FOREIGN KEY(Groups_id) REFERENCES Groups(id)
                );""")
        db_conn.commit()
    except sqlite3.OperationalError:
        print("Table SunsVoc couldn't be created")
#%%


###############################################################################        
if __name__ == '__main__':
    
    db_conn=sqlite3.connect(':memory:')
    
    CreateAllTables(db_conn)  
    
