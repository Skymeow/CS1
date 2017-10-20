# with open('sss.txt', r) as f
# give it write permission
# def clean_all_data(raw_text):
#     cleaned_data =
# with open('sales_data.txt','r') as f:
    #read all at once
    # text = f.read()
    # print first character of the line
    # print(text[0])
    # first_line = f.readline()
    # f.write("hello this is new")
    # save memory
    # f.close()
    # all_lines = list(f)
    # # get the first 10 lines
    # print(all_lines[:10])
    # get total sales number
    # numbers = 0
    # for i in f:
    #     sales_number = i.strip().split('\t')[3]
    #     number = sales_number.split('$')[1]
    #     numbers += float(number)
    # print(numbers)
    # maxsale = i.strip().split('\t')[3].split('$')[1]
    # get max sale city in Feb

    # first_line = list(f)[:1]
    # num = first_line[0].split('$')[1]
    # Q2 check = 2520
    # for i in f:
    #     all_text = i.strip().split('\t')[1]
    #     city = i.strip().split('\t')[0]
    #     # print(city)
    #     sale = float(i.strip().split('\t')[3].split('$')[1])
    #     month = int(all_text.split('/')[0])
    #     if month == 2:
    #         if sale>check:
    #             check = sale
    # print(check)
    # print(city)
# Q3
# with open('sales_data.txt','r') as f:
#     total = 0
#     for i in f:
#         all_text = i.strip().split('\t')[1]
#         payment_method = i.strip().split('\t')[2]
#         # print(payment_method)
#         money = i.strip().split('\t')[3]
#         item = float(money.split('$')[1])
#         # print(item)
#         if payment_method == "Cash":
#             total += item
#     print(total)

# Q4
# with open('sales_data.txt','r') as f:
#     cash = 0
#     baseball_cards = 0
#     credit = 0
#     check = 0
#     for i in f:
#         all_text = i.strip().split('\t')[1]
#         payment_method = i.strip().split('\t')[2]
#         month = int(all_text.split('/')[0])
#         city = i.strip().split('\t')[0]
#         if month == 3:
#             if city == "Oakland":
#                 if payment_method == "Cash":
#                    cash += 1
#                 elif payment_method == "Baseball Cards":
#                     baseball_cards += 1
#                 elif payment_method == "Credit":
#                     credit += 1
#                 elif payment_method == "Check":
#                     check += 1
#     list = {"cash":cash, "baseball":baseball_cards, "credit":credit, "check":check}
#     result = max(list.values())
#     for k,v in list.items():
#         if v == result:
#             print(k)

# Q5
with open('sales_data.txt','r') as f:
    # get tatol $ of credit
    amount_total = 0
    total = 0
    for i in f:
        all_text = i.strip().split('\t')[1]
        payment_method = i.strip().split('\t')[2]
        sales_number = i.strip().split('\t')[3]
        money = float(sales_number.split('$')[1])
        if payment_method == "Credit":
           amount_total += money
           total += 1
    print(amount_total/total)










