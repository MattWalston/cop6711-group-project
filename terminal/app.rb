require 'pry'

require_relative 'tweet'

# TODO: refactor into singleton object or perhaps move to db if needed

FEATURES = {
    economy: %w(economy),
    environment: %w(quality environmental bionomics ecology bionomic ecology sentience knowingness knowledge awareness cognisance conscious resource imagination resourcefulness sustainability sustainable),
    governance: [],
    people: [],
    mobility: [],
    living: []
}

# stemify due to differing algorithms
FEATURES.each_key do |key|
  FEATURES[key].map!(&:stem)
end


# TODO: make dynamic
tweet = Tweet.new "I want some damn ecology sentience in my backyard from some awareness."
related_features = tweet.related_to_features FEATURES

puts related_features
