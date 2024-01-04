#!/usr/bin/env ruby
#regular expression phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
