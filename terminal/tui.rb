require 'pry'

require_relative 'subject'
require_relative 'terms'

# TODO: make dynamic
tweet = Subject.new "I want some damn ecology sentience in my backyard from some awareness."
related_features = tweet.related_to_features Terms.instance.terms
puts related_features

