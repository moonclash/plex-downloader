from thefuzz import fuzz

class FuzzyMatch:
    
    def __init__(self) -> None:
        pass

    def get_phrase_ratio(self, original, target):
        return fuzz.ratio(original.lower(), target.lower())
    
    def is_phrase_in_list(self, phrase, list_):
        ratios = [self.get_phrase_ratio(phrase, list_phrase) for list_phrase in list_]
        return any([ratio >= 30 for ratio in ratios])