Python script to randomly select single line json objects from a file and build up bulk post data and post against the \_bulk API of Elasticsearch
 
Example:
```sh
$ ./es-bulk-process.py --host elasticsearch.mynetwork.local --index test-bulk --index-type bulktype --bulk-size 200 --count 10 --file files/data.json
```

This will generate a bulk post body payload of 200 documents that are randomly selected from the file _files/data.json_ 10 times.  This will total 2000 documents of type _bulktype_ in the index _test-bulk_

Help:
```sh
simon.thorley@simonpc-fed es-bulk-loader:master±]$ ./es-bulk-process.py --help
Usage: es-bulk-process.py [options]

Options:
  -h, --help            show this help message and exit
  -T BULKTYPE, --bulk-type=BULKTYPE
                        Type of bulk input (index,delete,update)
  -f FILENAME, --file=FILENAME
                        File with the source data
  -H ESHOST, --host=ESHOST
                        The elasticsearch destination host
  -P ESPORT, --port=ESPORT
                        The elasticsearch destination Port
  -s, --ssl             Use HTTPS instead of HTTP
  -i ESINDEX, --index=ESINDEX
                        The index on the elasticsearch cluster to call
  -c BULKCOUNT, --count=BULKCOUNT
                        The count of bulks to run (bulkscount * bulk-size =
                        total documents)
  -b BULKSIZE, --bulk-size=BULKSIZE
                        The amount of documents in each bulk API POST
  -t INDEXTYPE, --index-type=INDEXTYPE
                        The type of document in the index
  -u ESUSER, --user=ESUSER
                        Username for the elasticsearch URL
  -p ESPASS, --pass=ESPASS
                        Password for the elasticsearch URL
```

Note:
Only the index action works currently
