require 'tokenizer'
require 'stemmify'

THRESHOLD_COUNT = 2
THRESHOLD_DENSITY = 0.15 # TODO: Not yet implemented

$tokenizer = Tokenizer::WhitespaceTokenizer.new

class Tweet
  attr_reader :body, :parsed

  def initialize(body)
    @body = body
    @parsed = $tokenizer.tokenize(@body)
                  .map(&:downcase)
                  .map(&:stem)
  end

  def feature_count(feature_array)
    matched_features(feature_array).count
  end

  def matched_features(feature_array)
    @parsed & feature_array
  end

  def related_to_by_count?(feature_array)
    THRESHOLD_COUNT <= feature_count(feature_array)
  end

  def related_to_features(feature_array_hash)
    feature_array_hash.filter {|_, v| related_to_by_count? v}.keys
  end
end