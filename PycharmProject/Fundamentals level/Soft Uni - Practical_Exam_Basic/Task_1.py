bitcoin = float(input())
ch_una = float(input())
commission = float(input())

bit = bitcoin * 1168
ch = ch_una * 0.15
ch_lv = ch * 1.76

total = (bit + ch_lv) / 1.95

com = total * commission/100

result = total - com

print(f'{result: .2f}')
