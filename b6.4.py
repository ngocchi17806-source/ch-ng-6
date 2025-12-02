print('nguyen ngoc chi mssv 245752021610164')
class RomanToInteger:
    def __init__(self):
        #Mappings of Roman numerals to integer values
        self.roman_map = {
            'I':1, 'V':5, 'X':10, 'L':50,
            'C': 100,'D': 500,'M':1000
            }
        def convert(self, roman: str) -> int:
            #Ket qua ban dau la 0
            result = 0
            #Duyet qua cac ky tu trong chuoi La Ma
            for i in range(len(roman)):
                #lay gia tri cua ky tu hien tai
                current_value = self.roman_map[roman[i]]
                #Kiem tra neu ky tu hien tai co gia tri nho hon ky tu tiep theo
                #thi tru di gia tri cua ky tu hien tai, neu khong cong vao
                if i +1 < len(roman) and current_value < self.roman_map[roman[i+1]]:
                    result -= current_value
                else:
                    result += current_value
            return result
        #Test chuong trinh
    if __name__ == "__main__":
        roman_converter = RomanToInteger()
        #Thu nghiem voi mot so La Ma
        roman_numeral = "XVI"
        print(f"So La Ma {roman_numeral} chuyen thanh so nguyen la:{roman_converter.convert(roman_numeral)}")
        roman_numeral = "MMX"
        print(f"So La Ma {roman_numeral} chuyen thanh so nguyen la:{roman_converter.convert(roman_numeral)}")
