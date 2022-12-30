a = int(input("Vizenizi Girin:"))
b = int(input("Finaliniz Girin:"))
c = a * 4/10 + b * 6/10
f =int((50 - a * 4/10) * 10/6)
if (c >= 50):
  print("{} İle Geçtiniz".format(c))
else:
  print("{} İle Kaldınız,Geçmek için en az {} almanız lazım !".format(c,f))
