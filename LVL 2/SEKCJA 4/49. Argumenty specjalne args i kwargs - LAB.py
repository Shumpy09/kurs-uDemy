def Calculate_paint(efficency_ltr_per_m2, *args):
    
    print("Do pomalowania 1m2 porzeba: {} litrow farby".format(efficency_ltr_per_m2))
    print("Ilosc pokoi do pomalowania: {}. Powierzchnie pokoi: {}".format(len(args), args))
    
    for i in args:
        result = i / efficency_ltr_per_m2
        print("Do pomalowania {} pokoju potrzeba {} litrow farby".format(i,result))

Calculate_paint(1, 10, 20, 30)

room_list = [5,10,15]
print(30*'-')
Calculate_paint(1, *room_list)

'''
def calculate_paint(efficency_ltr_per_m2, *rooms):
    total_area = sum(rooms)
    paint = total_area * efficency_ltr_per_m2
    return paint

print(calculate_paint(0.25,42,28,30))
rooms = [42,28,30]
print(calculate_paint(0.25,*rooms))
'''