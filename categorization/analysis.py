
# from sklearn.neural_network import MLPClassifier

from categorization.text_parsing import Digestor, CONSTANTS
from categorization.metrics import VALUES


class TextAnalyzer(object):

    digestor = None

    def __init__(self):
        self.digestor = Digestor()

    def analyze(self, text):

        results = self.digestor.digest(text)

        return results

    def _format_data(self, data_dict):
        """
        Formats the results dict into an ordered list with frequencies
        :param data_dict:
        :return:
        """
        charset = VALUES.CHARSET
        data_dict = dict(data_dict)

        data = []

        for char in charset:
            data.append(data_dict.get(char, 0.0))

        return data


if __name__ == "__main__":

    test_data = {"#": 0.010895883777239709, "\"": 0.009685230024213076, "$": 0.0012106537530266344, "'": 0.009685230024213076, "&": 0.0012106537530266344, ")": 0.007263922518159807, "(": 0.00847457627118644, "+": 0.0012106537530266344, "-": 0.04600484261501211, "/": 0.06416464891041163, "1": 0.1016949152542373, "0": 0.07506053268765134, "3": 0.021791767554479417, "2": 0.053268765133171914, "5": 0.0387409200968523, "4": 0.012106537530266344, "7": 0.023002421307506054, "6": 0.03026634382566586, "9": 0.0387409200968523, "8": 0.043583535108958835, "=": 0.20823244552058112, "?": 0.0012106537530266344, "A": 0.09200968523002422, "@": 0.18038740920096852, "C": 0.06416464891041163, "B": 0.04721549636803874, "E": 0.0847457627118644, "D": 0.05205811138014528, "G": 0.002421307506053269, "F": 0.023002421307506054, "I": 0.04721549636803874, "H": 0.029055690072639227, "K": 0.018159806295399514, "J": 0.015738498789346248, "M": 0.04600484261501211, "L": 0.05447941888619855, "O": 0.05447941888619855, "N": 0.044794188861985475, "Q": 0.0036319612590799033, "P": 0.03268765133171913, "S": 0.06416464891041163, "R": 0.03026634382566586, "U": 0.026634382566585957, "T": 0.0811138014527845, "W": 0.012106537530266344, "V": 0.00847457627118644, "Y": 0.010895883777239709, "X": 0.010895883777239709, "Z": 0.006053268765133172, "_": 0.006053268765133172, "a": 0.9418886198547215, "c": 0.4116222760290557, "b": 0.19975786924939468, "e": 1.0, "d": 0.42857142857142855, "g": 0.14043583535108958, "f": 0.11259079903147699, "i": 0.6234866828087167, "h": 0.33777239709443097, "k": 0.23486682808716708, "j": 0.03631961259079903, "m": 0.32566585956416466, "l": 0.44552058111380144, "o": 0.6682808716707022, "n": 0.6210653753026635, "q": 0.004842615012106538, "p": 0.17796610169491525, "s": 0.6246973365617433, "r": 0.4854721549636804, "u": 0.22276029055690072, "t": 0.612590799031477, "w": 0.1585956416464891, "v": 0.08353510895883777, "y": 0.1343825665859564, "x": 0.010895883777239709, "z": 0.018159806295399514, "|": 0.0012106537530266344}

    ta = TextAnalyzer()
    # print ta.analyze("This is a test -- 1 2 3 1 2 3 4 1 2 3 4 5 5 6")
    print ta._format_data(test_data)

