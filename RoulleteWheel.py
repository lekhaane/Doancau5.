from random import randint
def roulette(green, yellow, red):
  total = green + yellow + red
  quay = randint(1, total)
  if quay <= green:
    return "Xanh"
  elif quay <= green + yellow:
    return "Vàng"
  else:
    return "Đỏ"
for params in [[47, 3, 50], [17, 3, 50], [77, 3, 50]]:
  green, yellow, red = params
  kq = {"Xanh": 0, "Vàng": 0, "Đỏ": 0}
  for i in range(10):
    kq[roulette(green, yellow, red)] += 1
  print(f"Bộ tham số: {green} xanh, {yellow} vàng, {red} đỏ")
  for color, count in kq.items():
    print(f" - {color}: {count}")

