pages_In_Book = int(input())
pages_Per_Hour = int(input())
days_Whole_Book = int(input())

whole_Time = pages_In_Book / pages_Per_Hour
hours_Per_Day = whole_Time / days_Whole_Book

print(hours_Per_Day)