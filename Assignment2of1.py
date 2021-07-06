days = [1,2,3,4,5,6,7]
sales_1 = [160, 150, 140, 145, 175, 165, 180]
sales_2 = [70, 90, 160, 150, 140, 145, 175]
plt.figure(figsize=(6,5), dpi=150)
plt.plot(days, sales_1,label='sales_1',marker='o')
plt.plot(days, sales_2,label='sales_2',marker='*')
plt.title('Sales distribution',color='slateblue')
plt.xlabel('days of the week',color='grey')
plt.ylabel('sales',color='grey')
plt.legend(loc='lower right')
plt.grid()