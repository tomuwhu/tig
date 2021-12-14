import locale
import time
locale.setlocale(locale.LC_ALL, 'hu_HU')
print( f'Mai dátum: {time.strftime("%Y. %B %d. ( %A )")}' )