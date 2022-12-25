import codecs

def input_AD():
    while(True):
        year = input("西暦を入力してください：")
        if(year.isdigit()):
            break
    return int(year)

# 閏年
def leap(year):
    if (year%400 == 0) or ((year%4 == 0) and (year%100 != 0))  :
        return 1;
    else:
        return 0;

# ツェラーの公式
def ZellersCongruence(year,month,day):
    if month < 3 :
        year-=1
        month+=12
    return (year + year//4 - year//100 + year//400 + (13 * month + 8) // 5 + day ) % 7

# 曜日
def week_of_day_str():
    w_str = "\\begingroup\n"
    w_str += "\\renewcommand{\\arraystretch}{1.4}\n"
    w_str += "\\begin{tabular}{|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|}\n"
    w_str += "\\hline\n"
    w_str += "\\large Sunday&\\large Monday &\\large Tuesday&\\large Wednesday&\\large Thursday&\\large Friday&\\large Saturday\\\\\n"
    w_str += "\\hline\n"
    w_str += "\\end{tabular}\n"
    w_str += "\\endgroup\n\n"
    return w_str

def calendar(year):
    month_date = [31,28+leap(year),31,30,31,30,31,31,30,31,30,31]
    # month_name = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    cale_str = ""
    for month in range(1,13):
        count = ZellersCongruence(year,month,1)
        cale_str += "\\begin{center}\n"
        cale_str += "\t\\LARGE " + str(year) + "年\\\\\n"
        cale_str += "\t\\LARGE " + str(month) + "月\n"
        cale_str += "\\end{center}\n"
        cale_str += "\n"
        cale_str += week_of_day_str()
        cale_str += "\\begingroup\n"
        cale_str += "\\renewcommand{\\arraystretch}{4}\n"
        cale_str += "\\begin{tabular}{|p{32mm}|p{32mm}|p{32mm}|p{32mm}|p{32mm}|p{32mm}|p{32mm}|}\n"
        cale_str += "\\hline\n"
        for week in range(ZellersCongruence(year,month,1)):
            cale_str += "&"
        for day in range(1,month_date[month - 1] + 1):
            cale_str += "\\raisebox{30pt} {"
            if day < 10:
                cale_str += "\\dig"
            else :
                cale_str += "\\tdig"
            cale_str += "\\LBF{"+ str(day) +"}}"
            count += 1
            if count%7 == 0 :
                cale_str += "\\\\\n"
                cale_str += "\\hline\n"
            else:
                cale_str += "&"
        marge = 5 - ZellersCongruence(year,month,month_date[month - 1])
        for blank in range (marge):
            cale_str += "&"
        if marge >= 0:
            cale_str += "\\\\\n"
            cale_str += "\\hline\n"
        cale_str += "\\end{tabular}\n"
        cale_str += "\\endgroup\n"
        cale_str += "\\newpage"
    cale_str += "\\end{document}"

    return cale_str




def ganerate_calender(year):
    path = "./calender.tex"
    # ファイルを開く（上書き）
    f = codecs.open(path,"w","utf-8")

    str =  "\\documentclass[a4paper,landscape]{jsarticle}\n"
    str += "\n"
    str += "\\usepackage[top=1cm , bottom = 1cm , left = 2cm , right = 2cm , includefoot]{geometry}\n"
    str += "\\usepackage{array}\n"
    str += "\n"
    str += "\\newcommand{\\dig}{\\hspace{29mm}}\n"
    str += "\\newcommand{\\tdig}{\\hspace{27mm}}\n"
    str += "\\newcommand{\\LBF}{\\LARGE\\textbf}\n"
    str += "\n"
    str += "\\begin{document}\n"
    str += "\n"
    str += "\\pagestyle{empty}\n"
    str += "\n"
    f.write(str)

    str = calendar(year)

    f.write(str)

    f.close()

def main():
    ganerate_calender(input_AD())


if __name__ == "__main__":
    main()
