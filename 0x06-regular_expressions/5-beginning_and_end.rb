#!/usr/bin/env ruby
# This script that match string starting with h and ends with b and having any
# character in between
puts ARGV[0].scan(/^h.n/).join
