table_metadata = {
    "TableMetadata": {
        "Name": "test_table",
        "CreateTime": 1593559968.0,
        "LastAccessTime": 0.0,
        "TableType": "EXTERNAL_TABLE",
        "Columns": [
            {
                "Name": "Column1",
                "Type": "string",
                "Comment": "from deserializer"
            },
            {
                "Name": "Column2",
                "Type": "int",
                "Comment": "from deserializer"
            },
            {
                "Name": "Column3",
                "Type": "date",
                "Comment": "from deserializer"
            }
        ],
        "PartitionKeys": [],
        "Parameters": {
            "EXTERNAL": "TRUE",
            "inputformat": "com.esri.json.hadoop.EnclosedJsonInputFormat",
            "location": "s3://awsdoc-example-bucket/json",
            "outputformat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
            "serde.param.serialization.format": "1",
            "serde.serialization.lib": "com.esri.hadoop.hive.serde.JsonSerde",
            "transient_lastDdlTime": "1593559968"
        }
    }
}

table_name = table_metadata['TableMetadata']['Name']
table_columns = table_metadata['TableMetadata']['Columns']

arquivo = open(table_name+".yaml", 'w+')
arquivo.writelines('TableName: '+table_name+'\n'
                    'DataQualityCheck: TRUE\n'
                    'Asserts:\n'
                    '  NumberOfColumns: '+str(len(table_columns))+'\n')

for column in table_columns:
    arquivo.writelines('  '+column.get('Name')+': '+column.get('Type')+'\n')

arquivo.close()
