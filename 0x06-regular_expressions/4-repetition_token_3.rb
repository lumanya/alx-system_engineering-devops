#!/usr/bin/env ruby
# This script use repition token to search for string
puts ARGV[0].scan(/hbt{,4}?n/).join
