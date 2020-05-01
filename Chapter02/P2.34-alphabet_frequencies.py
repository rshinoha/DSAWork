# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Project exercise P-2.34
# Ryoh Shinohara
# =======================================================================================
# Write a Python program that inputs a document and then outputs a bar chart plot of the
# frequencies of each alphabet character that appears in that document.

# Set chart height to 26 lines on console
CHART_HEIGHT = 26
# Number of lines in between major ticks
MINOR_TICK_SECTION = 5
# Integer representation of 'a'
A = ord('a')
# Number of letters in the alphabet
NUM_LETTERS = 26

class BarChart():
    """Creates bar chart based on dictionary data"""
    def __init__(self, data, sort_value=True, symbol='#'):
        """
        Creates bar chart object
        
        * data: dictionary containing variable names as keys and counts as values
        * sort_value: whether bar chart should be sorted by value or not; default
          True; if False, sorts by keys lexicographically
        * symbol: symbol to use for bars
        """
        if isinstance(data, dict):
            if all([isinstance(v, int) for v in data.values()]):
                self._data = data
            else:
                raise TypeError('values must be numeric')
        else:
            raise TypeError('data must be a dictionary')
        self._sort_value = sort_value
        self._symbol = symbol

    def get_data(self):
        """Returns dictionary of data"""
        return self._data

    def get_sort_value(self):
        """Returns whether bar chart will be sorted by value or not"""
        return self._sort_value

    def get_symbol(self):
        """Returns the symbol that will be used for bars"""
        return self._symbol

    def _determine_ticks(self):
        """Determines major and minor tick values"""
        major = 0
        max_num = max(self._data.values())
        if max_num > 1000:
            raise ValueError('data values must be less than 1000')
        elif max_num > 500:
            major = 200
        elif max_num > 100:
            major = 100
        elif max_num > 50:
            major = 10
        else:
            major = 5
        minor = major // MINOR_TICK_SECTION
        return major, minor

    def _determine_bar_heights(self, major, minor, sorted_list):
        """Determines bar heights for each data value"""
        bar_heights = []
        for i in sorted_list:
            bar_heights.append(CHART_HEIGHT - 1 - (self._data[i] // major + self._data[i] // minor))
        return bar_heights

    def plot(self):
        """
        A very naive implementation for plotting a bar chart of the data as a
        list of strings
        
        Limitations:
        * Will only tolerate max value counts of 1000
        * Inflexible axis tick marks
        * When in between minor tick marks, the value will be rounded down
        """
        # Stores bar chart as list of strings
        chart = []
        if self._sort_value:
            sorted_data = sorted(self._data, key=self._data.__getitem__, reverse=True)
        else:
            sorted_data = sorted(self._data)
        major, minor = self._determine_ticks()
        # Padding added for major tick value strings shorter than the max value
        # string length
        left_padding = len(str(major * (CHART_HEIGHT // MINOR_TICK_SECTION)))
        bar_heights = self._determine_bar_heights(major, minor, sorted_data)
        count = CHART_HEIGHT // MINOR_TICK_SECTION
        for i in range(CHART_HEIGHT - 1):
            temp_str = ''
            if i % MINOR_TICK_SECTION == 0 and CHART_HEIGHT // MINOR_TICK_SECTION != 0:
                temp_str += ' ' * (left_padding - len(str(major * count))) + str(major * count) + '| '
                count -= 1
            else:
                temp_str += ' ' * left_padding + '| '
            for j in range(len(sorted_data)):
                if i < bar_heights[j]:
                    temp_str += ' ' * 4
                else:
                    temp_str += self._symbol * 3 + ' '
            chart.append(temp_str)
        temp_str = ' ' * left_padding + '|_'
        for j in range(len(sorted_data)):
            if bar_heights[j] < CHART_HEIGHT - 1:
                temp_str += self._symbol * 3 + '_'
            else:
                temp_str += '_' * 4
        chart.append(temp_str)
        temp_str = ' ' * (left_padding + 2)
        for j in range(len(sorted_data)):
            temp_str += ' ' + sorted_data[j] + '  '
        chart.append(temp_str)
        return chart
        
def read_doc(doc):
    """
    Takes in a document name and returns the count of each letter found in
    the document as a dictionary
    """
    letters = [chr(i + A) for i in range(NUM_LETTERS)]
    # Initialize dictionary of letters with 0 as values
    chr_dict = {key: 0 for key in letters}
    with open(doc, 'r') as reader:
        for line in reader:
            lower = line.lower()
            for c in lower:
                if c.isalpha():
                    chr_dict[c] += 1
    return chr_dict

def print_chart(chart):
    """Prints bar chart"""
    for i in chart:
        print(i)

if __name__ == "__main__":
    doc = "more_progressions.py"
    chr_dict = read_doc(doc)
    bar = BarChart(chr_dict)
    chart = bar.plot()
    print_chart(chart)