#!/usr/bin/env python

from optparse import OptionParser
from elasticsearch import Elasticsearch

parser = OptionParser()
parser.add_option("-T", "--bulk-type", dest="BulkType", help="Type of bulk input (index,delete,update)", default="index")
parser.add_option("-f", "--file", dest="FileName", help="File with the source data")
parser.add_option("-U", "--url", dest="EsUrl", help="The elasticsearch destination URL including port")
parser.add_option("-s", "--ssl", dest="SSL", help="Use HTTPS instead of HTTP", default="http", action
parser.add_option("-i", "--index", dest="EsIndex", help="The index on the elasticsearch cluster to call")
parser.add_option("-c", "--count", dest="BulkCount", help="The count of records to run")
parser.add_option("-b", "--bulk-size", dest="BulkSize", help="The amount of documents in each bulk API POST", default=100)
parser.add_option("-t", "--index-type", dest="IndexType", help="The type of document in the index")
parser.add_option("-u", "--user", dest="EsUser", help="Username for the elasticsearch URL")
parser.add_option("-p", "--pass", dest="EsPass", help="Password for the elasticsearch URL")
parser.add_option("-d", "--debug", dest="Debug", action="store_true", default=False, help="Enable debug mode, no write out to ES")

(options, args) = parser.parse_args()

if options.Debug == False:
    if not options.EsUrl:
        print "Elasticsearch URL is required"
        parser.print_help()
        sys.exit(1)
    elif not options.BulkCount:
        print "Run count value is required"
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
    else:
        print "Using ES URL: " + options.EsUrl

es = Elasticsearch([options.EsUrl])
