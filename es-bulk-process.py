#!/usr/bin/env python

from optparse import OptionParser
from elasticsearch import Elasticsearch
import random

parser = OptionParser()
parser.add_option("-f", "--file", dest="FileName", help="File with the source data")
parser.add_option("-H", "--host", dest="EsHost", help="The elasticsearch destination host")
parser.add_option("-P", "--port", dest="EsPort", help="The elasticsearch destination Port", default="9200")
parser.add_option("-s", "--ssl", dest="SSL", help="Use HTTPS instead of HTTP", default=False, action="store_true")
parser.add_option("-i", "--index", dest="EsIndex", help="The index on the elasticsearch cluster to call")
parser.add_option("-c", "--count", dest="BulkCount", help="The count of bulks to run (bulkscount * bulk-size = total documents)", type="int")
parser.add_option("-b", "--bulk-size", dest="BulkSize", help="The amount of documents in each bulk API POST", type="int")
parser.add_option("-t", "--index-type", dest="IndexType", help="The type of document in the index")
parser.add_option("-u", "--user", dest="EsUser", help="Username for the elasticsearch URL")
parser.add_option("-p", "--pass", dest="EsPass", help="Password for the elasticsearch URL")

(options, args) = parser.parse_args()

if not options.EsHost:
    print "Elasticsearch host is required"
    parser.print_help()
    sys.exit(1)
elif not options.BulkCount:
    print "Run count value is required"
    parser.print_help()
    sys.exit(1)
elif not options.BulkSize:
    print "Document bulk size is required"
    parser.print_help()
    sys.exit(1)
elif not options.FileName:
    print "Source file is required"
    parser.print_help()
    sys.exit(1)
elif not options.EsIndex:
    print "Destination elasticsearch index is required"
    parser.print_help()
    sys.exit(1)
elif not options.IndexType:
    print "Destination index type is required"
    parser.print_help()
    sys.exit(1)

# Setup ES connection
if options.SSL:
    protocol = 'https://'
else:
    protocol = 'http://'

if options.EsUser and options.EsPass:
    es = Elasticsearch([protocol + options.EsUser + ':' + options.EsPass + '@' + options.EsHost + ':' + options.EsPort])
elif options.EsUser:
    es = Elasticsearch([protocol + options.EsUser + '@' + options.EsHost + ':' + options.EsPort])
else:
    es = Elasticsearch([options.EsHost + ':' + options.EsPort])

# Read in source file
with open(options.FileName, 'r') as f:
    filecontent = f.readlines()
print 'Read in ' + str(len(filecontent)) + ' lines from file...'

bulk = ''

print 'Processing ' + str(options.BulkCount) + ' bulk posts with ' + str(options.BulkSize) + ' documents in each making a total of ' + str(options.BulkCount * options.BulkSize)

for count in range(0,options.BulkCount):
    for size in range(0,options.BulkSize):
        bulk = bulk + ('{ "index": {}}\n')
        bulk = bulk + random.choice(filecontent).rstrip('\n') + '\n'
    bulk = bulk.rstrip('\n')
    es.bulk(body=bulk, index=options.EsIndex, doc_type=options.IndexType)
    bulk = ''

print "Bulk process complete..."
