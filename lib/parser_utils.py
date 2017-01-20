

class ParserUtils:

	@staticmethod
	def find_abv(text):
		return text[text.find("ABV"):].strip("ABV").strip()

	@staticmethod
	def find_name(text):
		return text[:text.find("ABV")].strip()

	@staticmethod
	def find_ibu(text):
		return text[text.find("IBU"):].strip("IBU").strip()

