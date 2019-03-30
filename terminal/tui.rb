#!/usr/bin/env ruby

require 'pry' if ENV['RUBY_ENV'] == 'development'

require_relative 'subject'
require_relative 'terms'

puts "Supply message to parse (LF submits):" if STDIN.tty?
body = gets

tweet = Subject.new body

related_features = tweet.related_to_features Terms.instance.terms

puts related_features.count > 1 ? related_features : 'No features identified.'

