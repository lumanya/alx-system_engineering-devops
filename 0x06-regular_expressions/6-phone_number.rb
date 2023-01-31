#!/usr/bin/env ruby
# This script macthc 10 phone numbers digits
puts ARGV[0].scan(/^\d{10}/).join
