require 'singleton'

TERMS_PATH = 'terms'

class Terms
  include Singleton

  def terms
    @terms ||= build_hash
  end

  def build_hash
    hash = {}

    Dir.foreach(TERMS_PATH) do |filename|
      next if filename == '.' or filename == '..'
      hash[filename] = array_from_file "#{TERMS_PATH}/#{filename}"
    end

    hash
  end

  def array_from_file(filename)
    File.readlines(filename)
        .map(&:strip)
        .map(&:downcase)
        .map(&:stem)
  end
end