import codecs
import os


def input_AD():
    while(True):
        year = input("西暦を入力してください：")
        if(year.isdigit()):
            break
    return int(year)

def setting_sun_color():
    clr_set = 1
    while(True):
        print("1...日曜日（Sunday）の曜日名と日付を黒にする\n")
        print("2...日曜日（Sunday）の曜日名を赤、日付を黒にする\n")
        print("3...日曜日（Sunday）の曜日名と日付を赤にする\n")
        print("4...日曜日（Sunday）の曜日名を赤、土曜日（Saturday）の曜日名を青、日付を黒にする\n")
        print("5...日曜日（Sunday）の曜日名と日付を赤、土曜日（Saturday）の曜日名と日付を青にする\n")

        color = input("日曜日の色を数字で指定してください：")
        if(color.isdigit()):
            clr_set = int(color)
            if (clr_set >= 1) and (clr_set <= 5):
                break
    return clr_set


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
def week_of_day_str(color):
    week_name = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    for i in range(7):
        week_name[i] = "\\large " + week_name[i]

    if color == 2 or color == 3 or color == 4 or color == 5:
        week_name[0] = "\\textcolor{red}{" + week_name[0] + "}"
    if color == 4 or color == 5:
        week_name[6] = "\\textcolor{blue}{" + week_name[6] + "}"


    w_str = "\\begingroup\n"
    w_str += "\\renewcommand{\\arraystretch}{1.4}\n"
    w_str += "\\begin{tabular}{|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|>{\\centering\\arraybackslash}p{32mm}|}\n"
    w_str += "\\hline\n"
    for i in range(7):
        if i >= 1:
            w_str += "&"
        w_str += week_name[i]
    w_str += "\\\\\n"

    w_str += "\\hline\n"
    w_str += "\\end{tabular}\n"
    w_str += "\\endgroup\n\n"
    return w_str

def calendar(year,color):
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
        cale_str += week_of_day_str(color)
        cale_str += "\\begingroup\n"
        cale_str += "\\renewcommand{\\arraystretch}{4}\n"
        cale_str += "\\begin{tabular}{|p{32mm}|p{32mm}|p{32mm}|p{32mm}|p{32mm}|p{32mm}|p{32mm}|}\n"
        cale_str += "\\hline\n"
        for week in range(ZellersCongruence(year,month,1)):
            cale_str += "&"

        day_str = []
        for day in range(1,month_date[month - 1] + 1):
            zc = ZellersCongruence(year,month,day)
            # 曜日の日付塗りつぶし設定
            if (((color == 3) or (color == 5)) and zc == 0) or (color == 5 and zc == 6):
                # 日曜日
                if zc == 0:
                    day_str.append("\\textcolor{red}{\\LBF{"+ str(day) +"}}}")
                # 土曜日 zc == 6
                else :
                    day_str.append("\\textcolor{blue}{\\LBF{"+ str(day) +"}}}")
            else:
                day_str.append("\\LBF{"+ str(day) +"}}")
        for day in range(1,month_date[month - 1] + 1):
            # 改行 or 次の列（1日目は必要ないので2日目以降）
            if day >= 2:
                if count%7 == 0 :
                    cale_str += "\\\\\n"
                    cale_str += "\\hline\n"
                else:
                    cale_str += "&"
            # 日付の入力
            cale_str += "\\raisebox{30pt} {"
            if day < 10:
                cale_str += "\\dig"
            else :
                cale_str += "\\tdig"
            cale_str += day_str[day-1]
            count += 1

        # 最後の週のあまり
        marge = 6 - ZellersCongruence(year,month,month_date[month - 1])
        for blank in range (marge):
            cale_str += "&"

        cale_str += "\\\\\n"
        cale_str += "\\hline"
        cale_str += "\n"
        cale_str += "\\end{tabular}\n"
        cale_str += "\\endgroup\n\n"
        if month != 12:
            cale_str += "\\newpage\n\n"
    cale_str += "\\end{document}"

    return cale_str




def ganerate_calendar(year,color):
    path = "./calendar/calendar.tex"

    # フォルダが無ければ作成
    if not os.path.exists('calendar'):
        os.mkdir('calendar')

    # ファイルを開く（上書き）
    f = codecs.open(path,"w","utf-8")

    str =  "\\documentclass[a4paper,landscape]{jsarticle}\n"
    str += "\n"
    str += "\\usepackage[top=1cm , bottom = 1cm , left = 2cm , right = 2cm , includefoot]{geometry}\n"
    str += "\\usepackage{array}\n"
    if color != 1:
        str += "\\usepackage{color}\n"
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

    str = calendar(year,color)

    f.write(str)

    f.close()

def main():
    ganerate_calendar(input_AD(),setting_sun_color())



if __name__ == "__main__":
    main()
