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

        color = input("曜日の色を数字で指定してください：")
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

# 元号
def eraname(year):
    era_str = ""
    if year >= 2019:
        era_str += "令和"
        if year == 2019:
            era_str += "元"
        else:
            era_str += str(year - 2019 + 1)
        era_str += "年"
    elif year >= 1989:
        era_str += "平成"
        if year == 1989:
            era_str += "元"
        else:
            era_str += str(year - 1989 + 1)
        era_str += "年"
    elif year >= 1926:
        era_str += "昭和"
        if year == 1926:
            era_str += "元"
        else:
            era_str += str(year - 1926 + 1)
        era_str += "年"
    elif year >= 1912:
        era_str += "大正"
        if year == 1912:
            era_str += "元"
        else:
            era_str += str(year - 1912 + 1)
        era_str += "年"
    elif year >= 1603:
        era_str += "江戸時代/"
        if year >= 1865:
            era_str += "慶応"
            if year == 1865:
                era_str += "元"
            else:
                era_str += str(year - 1865 + 1)
            era_str += "年"
        elif year >= 1864:
            era_str += "元治"
            if year == 1864:
                era_str += "元"
            else:
                era_str += str(year - 1864 + 1)
            era_str += "年"
        elif year >= 1861:
            era_str += "文久"
            if year == 1861:
                era_str += "元"
            else:
                era_str += str(year - 1861 + 1)
            era_str += "年"
        elif year >= 1860:
            era_str += "万延"
            if year == 1860:
                era_str += "元"
            else:
                era_str += str(year - 1860 + 1)
            era_str += "年"
        elif year >= 1855:
            era_str += "安政"
            if year == 1855:
                era_str += "元"
            else:
                era_str += str(year - 1855 + 1)
            era_str += "年"
        elif year >= 1848:
            era_str += "嘉永"
            if year == 1848:
                era_str += "元"
            else:
                era_str += str(year - 1848 + 1)
            era_str += "年"
        elif year >= 1845:
            era_str += "弘化"
            if year == 1845:
                era_str += "元"
            else:
                era_str += str(year - 1845 + 1)
            era_str += "年"
        elif year >= 1831:
            era_str += "天保"
            if year == 1831:
                era_str += "元"
            else:
                era_str += str(year - 1831 + 1)
            era_str += "年"
        elif year >= 1818:
            era_str += "文政"
            if year == 1818:
                era_str += "元"
            else:
                era_str += str(year - 1818 + 1)
            era_str += "年"
        elif year >= 1804:
            era_str += "文化"
            if year == 1804:
                era_str += "元"
            else:
                era_str += str(year - 1804 + 1)
            era_str += "年"
        elif year >= 1801:
            era_str += "享和"
            if year == 1801:
                era_str += "元"
            else:
                era_str += str(year - 1804 + 1)
            era_str += "年"
        elif year >= 1789:
            era_str += "寛政"
            if year == 1789:
                era_str += "元"
            else:
                era_str += str(year - 1789 + 1)
            era_str += "年"
        elif year >= 1781:
            era_str += "天明"
            if year == 1781:
                era_str += "元"
            else:
                era_str += str(year - 1781 + 1)
            era_str += "年"
        elif year >= 1772:
            era_str += "安永"
            if year == 1772:
                era_str += "元"
            else:
                era_str += str(year - 1772 + 1)
            era_str += "年"
        elif year >= 1764:
            era_str += "明和"
            if year == 1764:
                era_str += "元"
            else:
                era_str += str(year - 1764 + 1)
            era_str += "年"
        elif year >= 1751:
            era_str += "宝暦"
            if year == 1751:
                era_str += "元"
            else:
                era_str += str(year - 1751 + 1)
            era_str += "年"
        elif year >= 1748:
            era_str += "寛延"
            if year == 1748:
                era_str += "元"
            else:
                era_str += str(year - 1748 + 1)
            era_str += "年"
        elif year >= 1744:
            era_str += "延享"
            if year == 1744:
                era_str += "元"
            else:
                era_str += str(year - 1744 + 1)
            era_str += "年"
        elif year >= 1741:
            era_str += "寛保"
            if year == 1741:
                era_str += "元"
            else:
                era_str += str(year - 1741 + 1)
            era_str += "年"
        elif year >= 1736:
            era_str += "元文"
            if year == 1736:
                era_str += "元"
            else:
                era_str += str(year - 1736 + 1)
            era_str += "年"
        elif year >= 1716:
            era_str += "享保"
            if year == 1716:
                era_str += "元"
            else:
                era_str += str(year - 1716 + 1)
            era_str += "年"
        elif year >= 1711:
            era_str += "正徳"
            if year == 1711:
                era_str += "元"
            else:
                era_str += str(year - 1711 + 1)
            era_str += "年"
        elif year >= 1711:
            era_str += "正徳"
            if year == 1711:
                era_str += "元"
            else:
                era_str += str(year - 1711 + 1)
            era_str += "年"
        elif year >= 1704:
            era_str += "宝永"
            if year == 1704:
                era_str += "元"
            else:
                era_str += str(year - 1704 + 1)
            era_str += "年"
        elif year >= 1688:
            era_str += "元禄"
            if year == 1688:
                era_str += "元"
            else:
                era_str += str(year - 1688 + 1)
            era_str += "年"
        elif year >= 1684:
            era_str += "貞享"
            if year == 1684:
                era_str += "元"
            else:
                era_str += str(year - 1684 + 1)
            era_str += "年"
        elif year >= 1681:
            era_str += "天和"
            if year == 1681:
                era_str += "元"
            else:
                era_str += str(year - 1681 + 1)
            era_str += "年"
        elif year >= 1673:
            era_str += "延宝"
            if year == 1673:
                era_str += "元"
            else:
                era_str += str(year - 1673 + 1)
            era_str += "年"
        elif year >= 1661:
            era_str += "寛文"
            if year == 1661:
                era_str += "元"
            else:
                era_str += str(year - 1661 + 1)
            era_str += "年"
        elif year >= 1658:
            era_str += "万治"
            if year == 1658:
                era_str += "元"
            else:
                era_str += str(year - 1658 + 1)
            era_str += "年"
        elif year >= 1655:
            era_str += "明暦"
            if year == 1655:
                era_str += "元"
            else:
                era_str += str(year - 1655 + 1)
            era_str += "年"
        elif year >= 1652:
            era_str += "承応"
            if year == 1652:
                era_str += "元"
            else:
                era_str += str(year - 1652 + 1)
            era_str += "年"
        elif year >= 1648:
            era_str += "慶安"
            if year == 1648:
                era_str += "元"
            else:
                era_str += str(year - 1648 + 1)
            era_str += "年"
        elif year >= 1645:
            era_str += "正保"
            if year == 1645:
                era_str += "元"
            else:
                era_str += str(year - 1645 + 1)
            era_str += "年"
        elif year >= 1624:
            era_str += "寛永"
            if year == 1624:
                era_str += "元"
            else:
                era_str += str(year - 1624 + 1)
            era_str += "年"
        elif year >= 1615:
            era_str += "元和"
            if year == 1615:
                era_str += "元"
            else:
                era_str += str(year - 1615 + 1)
            era_str += "年"
        elif year >= 1596:
            era_str += "慶長"
            if year == 1596:
                era_str += "元"
            else:
                era_str += str(year - 1596 + 1)
            era_str += "年"
    elif year >= 1573:
        era_str += "安土桃山時代/"
        if year >= 1596:
            era_str += "慶長"
            if year == 1596:
                era_str += "元"
            else:
                era_str += str(year - 1596 + 1)
            era_str += "年"
        elif year >= 1593:
            era_str += "文禄"
            if year == 1593:
                era_str += "元"
            else:
                era_str += str(year - 1593 + 1)
            era_str += "年"
        elif year >= 1573:
            era_str += "天正"
            if year == 1573:
                era_str += "元"
            else:
                era_str += str(year - 1573 + 1)
            era_str += "年"
    elif year >= 1336:
        era_str += "安土桃山時代/"
        if year >= 1570:
            era_str += "元亀"
            if year == 1570:
                era_str += "元"
            else:
                era_str += str(year - 1570 + 1)
            era_str += "年"
        elif year >= 1558:
            era_str += "永禄"
            if year == 1558:
                era_str += "元"
            else:
                era_str += str(year - 1558 + 1)
            era_str += "年"
        elif year >= 1555:
            era_str += "弘治"
            if year == 1555:
                era_str += "元"
            else:
                era_str += str(year - 1555 + 1)
            era_str += "年"
        elif year >= 1532:
            era_str += "天文"
            if year == 1532:
                era_str += "元"
            else:
                era_str += str(year - 1532 + 1)
            era_str += "年"
        elif year >= 1528:
            era_str += "享禄"
            if year == 1528:
                era_str += "元"
            else:
                era_str += str(year - 1528 + 1)
            era_str += "年"
        elif year >= 1521:
            era_str += "大永"
            if year == 1521:
                era_str += "元"
            else:
                era_str += str(year - 1521 + 1)
            era_str += "年"
        elif year >= 1504:
            era_str += "永正"
            if year == 1504:
                era_str += "元"
            else:
                era_str += str(year - 1504 + 1)
            era_str += "年"
        elif year >= 1501:
            era_str += "文亀"
            if year == 1501:
                era_str += "元"
            else:
                era_str += str(year - 1501 + 1)
            era_str += "年"
        elif year >= 1492:
            era_str += "明応"
            if year == 1492:
                era_str += "元"
            else:
                era_str += str(year - 1492 + 1)
            era_str += "年"
        elif year >= 1489:
            era_str += "延徳"
            if year == 1489:
                era_str += "元"
            else:
                era_str += str(year - 1489 + 1)
            era_str += "年"
        elif year >= 1487:
            era_str += "長享"
            if year == 1487:
                era_str += "元"
            else:
                era_str += str(year - 1487 + 1)
            era_str += "年"
        elif year >= 1469:
            era_str += "文明"
            if year == 1469:
                era_str += "元"
            else:
                era_str += str(year - 1469 + 1)
            era_str += "年"
        elif year >= 1467:
            era_str += "応仁"
            if year == 1467:
                era_str += "元"
            else:
                era_str += str(year - 1467 + 1)
            era_str += "年"
        elif year >= 1466:
            era_str += "文正"
            if year == 1466:
                era_str += "元"
            else:
                era_str += str(year - 1466 + 1)
            era_str += "年"
        elif year >= 1461:
            era_str += "寛正"
            if year == 1461:
                era_str += "元"
            else:
                era_str += str(year - 1461 + 1)
            era_str += "年"
        elif year >= 1457:
            era_str += "長禄"
            if year == 1457:
                era_str += "元"
            else:
                era_str += str(year - 1457 + 1)
            era_str += "年"
        elif year >= 1455:
            era_str += "康正"
            if year == 1455:
                era_str += "元"
            else:
                era_str += str(year - 1455 + 1)
            era_str += "年"
        elif year >= 1452:
            era_str += "享徳"
            if year == 1452:
                era_str += "元"
            else:
                era_str += str(year - 1452 + 1)
            era_str += "年"
        elif year >= 1449:
            era_str += "宝徳"
            if year == 1449:
                era_str += "元"
            else:
                era_str += str(year - 1449 + 1)
            era_str += "年"
        elif year >= 1444:
            era_str += "文安"
            if year == 1444:
                era_str += "元"
            else:
                era_str += str(year - 1444 + 1)
            era_str += "年"
        elif year >= 1441:
            era_str += "嘉吉"
            if year == 1441:
                era_str += "元"
            else:
                era_str += str(year - 1441 + 1)
            era_str += "年"
        elif year >= 1429:
            era_str += "永享"
            if year == 1429:
                era_str += "元"
            else:
                era_str += str(year - 1429 + 1)
            era_str += "年"
        elif year >= 1428:
            era_str += "正長"
            if year == 1428:
                era_str += "元"
            else:
                era_str += str(year - 1428 + 1)
            era_str += "年"
        elif year >= 1394:
            era_str += "応永"
            if year == 1394:
                era_str += "元"
            else:
                era_str += str(year - 1394 + 1)
            era_str += "年"
        elif year >= 1384:
            era_str += "元中[南朝]"
            if year == 1384:
                era_str += "元"
            else:
                era_str += str(year - 1384 + 1)
            era_str += "年"
        elif year >= 1381:
            era_str += "弘和[南朝]"
            if year == 1381:
                era_str += "元"
            else:
                era_str += str(year - 1381 + 1)
            era_str += "年"
        elif year >= 1375:
            era_str += "天授[南朝]"
            if year == 1375:
                era_str += "元"
            else:
                era_str += str(year - 1375 + 1)
            era_str += "年"
        elif year >= 1372:
            era_str += "文中[南朝]"
            if year == 1372:
                era_str += "元"
            else:
                era_str += str(year - 1372 + 1)
            era_str += "年"
        elif year >= 1370:
            era_str += "建徳[南朝]"
            if year == 1370:
                era_str += "元"
            else:
                era_str += str(year - 1370 + 1)
            era_str += "年"
        elif year >= 1347:
            era_str += "正平[南朝]"
            if year == 1347:
                era_str += "元"
            else:
                era_str += str(year - 1347 + 1)
            era_str += "年"
        elif year >= 1340:
            era_str += "興国[南朝]"
            if year == 1340:
                era_str += "元"
            else:
                era_str += str(year - 1340 + 1)
            era_str += "年"
        elif year >= 1336:
            era_str += "延元[南朝]"
            if year == 1336:
                era_str += "元"
            else:
                era_str += str(year - 1336 + 1)
            era_str += "年"
    elif year >= 1185:
        era_str += "鎌倉時代/"
        if year >= 1334:
            era_str += "建武"
            if year == 1334:
                era_str += "元"
            else:
                era_str += str(year - 1334 + 1)
            era_str += "年"
        elif year >= 1331:
            era_str += "元弘"
            if year == 1331:
                era_str += "元"
            else:
                era_str += str(year - 1331 + 1)
            era_str += "年"
        elif year >= 1329:
            era_str += "元徳"
            if year == 1329:
                era_str += "元"
            else:
                era_str += str(year - 1329 + 1)
            era_str += "年"
        elif year >= 1326:
            era_str += "嘉暦"
            if year == 1326:
                era_str += "元"
            else:
                era_str += str(year - 1326 + 1)
            era_str += "年"
        elif year >= 1324:
            era_str += "正中"
            if year == 1324:
                era_str += "元"
            else:
                era_str += str(year - 1324 + 1)
            era_str += "年"
        elif year >= 1321:
            era_str += "元亨"
            if year == 1321:
                era_str += "元"
            else:
                era_str += str(year - 1321 + 1)
            era_str += "年"
        elif year >= 1319:
            era_str += "元応"
            if year == 1319:
                era_str += "元"
            else:
                era_str += str(year - 1319 + 1)
            era_str += "年"
        elif year >= 1317:
            era_str += "文保"
            if year == 1317:
                era_str += "元"
            else:
                era_str += str(year - 1317 + 1)
            era_str += "年"
        elif year >= 1312:
            era_str += "正和"
            if year == 1312:
                era_str += "元"
            else:
                era_str += str(year - 1312 + 1)
            era_str += "年"
        elif year >= 1311:
            era_str += "応長"
            if year == 1311:
                era_str += "元"
            else:
                era_str += str(year - 1311 + 1)
            era_str += "年"
        elif year >= 1308:
            era_str += "延慶"
            if year == 1308:
                era_str += "元"
            else:
                era_str += str(year - 1308 + 1)
            era_str += "年"
        elif year >= 1307:
            era_str += "徳治"
            if year == 1307:
                era_str += "元"
            else:
                era_str += str(year - 1307 + 1)
            era_str += "年"
        elif year >= 1303:
            era_str += "嘉元"
            if year == 1303:
                era_str += "元"
            else:
                era_str += str(year - 1303 + 1)
            era_str += "年"
        elif year >= 1302:
            era_str += "乾元"
            if year == 1302:
                era_str += "元"
            else:
                era_str += str(year - 1302 + 1)
            era_str += "年"
        elif year >= 1299:
            era_str += "正安"
            if year == 1299:
                era_str += "元"
            else:
                era_str += str(year - 1299 + 1)
            era_str += "年"
        elif year >= 1293:
            era_str += "永仁"
            if year == 1293:
                era_str += "元"
            else:
                era_str += str(year - 1293 + 1)
            era_str += "年"
        elif year >= 1288:
            era_str += "正応"
            if year == 1288:
                era_str += "元"
            else:
                era_str += str(year - 1288 + 1)
            era_str += "年"
        elif year >= 1278:
            era_str += "弘安"
            if year == 1278:
                era_str += "元"
            else:
                era_str += str(year - 1278 + 1)
            era_str += "年"
        elif year >= 1275:
            era_str += "建治"
            if year == 1275:
                era_str += "元"
            else:
                era_str += str(year - 1275 + 1)
            era_str += "年"
        elif year >= 1264:
            era_str += "文永"
            if year == 1264:
                era_str += "元"
            else:
                era_str += str(year - 1264 + 1)
            era_str += "年"
        elif year >= 1261:
            era_str += "弘長"
            if year == 1261:
                era_str += "元"
            else:
                era_str += str(year - 1261 + 1)
            era_str += "年"
        elif year >= 1260:
            era_str += "文応"
            if year == 1260:
                era_str += "元"
            else:
                era_str += str(year - 1260 + 1)
            era_str += "年"
        elif year >= 1259:
            era_str += "正元"
            if year == 1259:
                era_str += "元"
            else:
                era_str += str(year - 1259 + 1)
            era_str += "年"
        elif year >= 1257:
            era_str += "正嘉"
            if year == 1257:
                era_str += "元"
            else:
                era_str += str(year - 1257 + 1)
            era_str += "年"
        elif year >= 1256:
            era_str += "康元"
            if year == 1256:
                era_str += "元"
            else:
                era_str += str(year - 1256 + 1)
            era_str += "年"
        elif year >= 1249:
            era_str += "建長"
            if year == 1249:
                era_str += "元"
            else:
                era_str += str(year - 1249 + 1)
            era_str += "年"
        elif year >= 1247:
            era_str += "宝治"
            if year == 1247:
                era_str += "元"
            else:
                era_str += str(year - 1247 + 1)
            era_str += "年"
        elif year >= 1243:
            era_str += "寛元"
            if year == 1243:
                era_str += "元"
            else:
                era_str += str(year - 1243 + 1)
            era_str += "年"
        elif year >= 1239:
            era_str += "延応"
            if year == 1239:
                era_str += "元"
            else:
                era_str += str(year - 1239 + 1)
            era_str += "年"
        elif year >= 1238:
            era_str += "暦仁"
            if year == 1238:
                era_str += "元"
            else:
                era_str += str(year - 1238 + 1)
            era_str += "年"
        elif year >= 1235:
            era_str += "嘉禎"
            if year == 1235:
                era_str += "元"
            else:
                era_str += str(year - 1235 + 1)
            era_str += "年"
        elif year >= 1234:
            era_str += "文暦"
            if year == 1234:
                era_str += "元"
            else:
                era_str += str(year - 1234 + 1)
            era_str += "年"
        elif year >= 1233:
            era_str += "天福"
            if year == 1233:
                era_str += "元"
            else:
                era_str += str(year - 1233 + 1)
            era_str += "年"
        elif year >= 1232:
            era_str += "貞永"
            if year == 1232:
                era_str += "元"
            else:
                era_str += str(year - 1232 + 1)
            era_str += "年"
        elif year >= 1229:
            era_str += "寛喜"
            if year == 1229:
                era_str += "元"
            else:
                era_str += str(year - 1229 + 1)
            era_str += "年"
        elif year >= 1228:
            era_str += "安貞"
            if year == 1228:
                era_str += "元"
            else:
                era_str += str(year - 1228 + 1)
            era_str += "年"
        elif year >= 1225:
            era_str += "嘉禄"
            if year == 1225:
                era_str += "元"
            else:
                era_str += str(year - 1225 + 1)
            era_str += "年"
        elif year >= 1224:
            era_str += "元仁"
            if year == 1224:
                era_str += "元"
            else:
                era_str += str(year - 1224 + 1)
            era_str += "年"
        elif year >= 1222:
            era_str += "貞応"
            if year == 1222:
                era_str += "元"
            else:
                era_str += str(year - 1222 + 1)
            era_str += "年"
        elif year >= 1219:
            era_str += "承久"
            if year == 1219:
                era_str += "元"
            else:
                era_str += str(year - 1219 + 1)
            era_str += "年"
        elif year >= 1214:
            era_str += "建保"
            if year == 1214:
                era_str += "元"
            else:
                era_str += str(year - 1214 + 1)
            era_str += "年"
        elif year >= 1211:
            era_str += "建暦"
            if year == 1211:
                era_str += "元"
            else:
                era_str += str(year - 1211 + 1)
            era_str += "年"
        elif year >= 1207:
            era_str += "承元"
            if year == 1207:
                era_str += "元"
            else:
                era_str += str(year - 1207 + 1)
            era_str += "年"
        elif year >= 1206:
            era_str += "建永"
            if year == 1206:
                era_str += "元"
            else:
                era_str += str(year - 1206 + 1)
            era_str += "年"
        elif year >= 1204:
            era_str += "元久"
            if year == 1204:
                era_str += "元"
            else:
                era_str += str(year - 1204 + 1)
            era_str += "年"
        elif year >= 1201:
            era_str += "建仁"
            if year == 1201:
                era_str += "元"
            else:
                era_str += str(year - 1201 + 1)
            era_str += "年"
        elif year >= 1199:
            era_str += "正治"
            if year == 1199:
                era_str += "元"
            else:
                era_str += str(year - 1199 + 1)
            era_str += "年"
        elif year >= 1190:
            era_str += "建久"
            if year == 1190:
                era_str += "元"
            else:
                era_str += str(year - 1190 + 1)
            era_str += "年"
        elif year >= 1185:
            era_str += "文治"
            if year == 1185:
                era_str += "元"
            else:
                era_str += str(year - 1185 + 1)
            era_str += "年"
    elif year >= 794:
        era_str += "平安時代/"
        if year >= 1184:
            era_str += "元暦"
            if year == 1184:
                era_str += "元"
            else:
                era_str += str(year - 1184 + 1)
            era_str += "年"
        elif year >= 1182:
            era_str += "寿永"
            if year == 1182:
                era_str += "元"
            else:
                era_str += str(year - 1182 + 1)
            era_str += "年"
        elif year >= 1181:
            era_str += "養和"
            if year == 1181:
                era_str += "元"
            else:
                era_str += str(year - 1181 + 1)
            era_str += "年"
        elif year >= 1177:
            era_str += "治承"
            if year == 1177:
                era_str += "元"
            else:
                era_str += str(year - 1177 + 1)
            era_str += "年"
        elif year >= 1175:
            era_str += "安元"
            if year == 1175:
                era_str += "元"
            else:
                era_str += str(year - 1175 + 1)
            era_str += "年"
        elif year >= 1171:
            era_str += "承安"
            if year == 1171:
                era_str += "元"
            else:
                era_str += str(year - 1171 + 1)
            era_str += "年"
        elif year >= 1169:
            era_str += "嘉応"
            if year == 1169:
                era_str += "元"
            else:
                era_str += str(year - 1169 + 1)
            era_str += "年"
        elif year >= 1166:
            era_str += "仁安"
            if year == 1166:
                era_str += "元"
            else:
                era_str += str(year - 1166 + 1)
            era_str += "年"
        elif year >= 1165:
            era_str += "永万"
            if year == 1165:
                era_str += "元"
            else:
                era_str += str(year - 1165 + 1)
            era_str += "年"
        elif year >= 1163:
            era_str += "長寛"
            if year == 1163:
                era_str += "元"
            else:
                era_str += str(year - 1163 + 1)
            era_str += "年"
        elif year >= 1161:
            era_str += "応保"
            if year == 1161:
                era_str += "元"
            else:
                era_str += str(year - 1161 + 1)
            era_str += "年"
        elif year >= 1160:
            era_str += "永暦"
            if year == 1160:
                era_str += "元"
            else:
                era_str += str(year - 1160 + 1)
            era_str += "年"
        elif year >= 1159:
            era_str += "平治"
            if year == 1159:
                era_str += "元"
            else:
                era_str += str(year - 1159 + 1)
            era_str += "年"
        elif year >= 1156:
            era_str += "保元"
            if year == 1156:
                era_str += "元"
            else:
                era_str += str(year - 1156 + 1)
            era_str += "年"
        elif year >= 1154:
            era_str += "久寿"
            if year == 1154:
                era_str += "元"
            else:
                era_str += str(year - 1154 + 1)
            era_str += "年"
        elif year >= 1151:
            era_str += "仁平"
            if year == 1151:
                era_str += "元"
            else:
                era_str += str(year - 1151 + 1)
            era_str += "年"
        elif year >= 1145:
            era_str += "久安"
            if year == 1145:
                era_str += "元"
            else:
                era_str += str(year - 1145 + 1)
            era_str += "年"
        elif year >= 1144:
            era_str += "天養"
            if year == 1144:
                era_str += "元"
            else:
                era_str += str(year - 1144 + 1)
            era_str += "年"
        elif year >= 1142:
            era_str += "康治"
            if year == 1142:
                era_str += "元"
            else:
                era_str += str(year - 1142 + 1)
            era_str += "年"
        elif year >= 1141:
            era_str += "永治"
            if year == 1141:
                era_str += "元"
            else:
                era_str += str(year - 1141 + 1)
            era_str += "年"
        elif year >= 1135:
            era_str += "保延"
            if year == 1135:
                era_str += "元"
            else:
                era_str += str(year - 1135 + 1)
            era_str += "年"
        elif year >= 1132:
            era_str += "長承"
            if year == 1132:
                era_str += "元"
            else:
                era_str += str(year - 1132 + 1)
            era_str += "年"
        elif year >= 1131:
            era_str += "天承"
            if year == 1131:
                era_str += "元"
            else:
                era_str += str(year - 1131 + 1)
            era_str += "年"
        elif year >= 1126:
            era_str += "大治"
            if year == 1126:
                era_str += "元"
            else:
                era_str += str(year - 1126 + 1)
            era_str += "年"
        elif year >= 1124:
            era_str += "天治"
            if year == 1124:
                era_str += "元"
            else:
                era_str += str(year - 1124 + 1)
            era_str += "年"
        elif year >= 1120:
            era_str += "保安"
            if year == 1120:
                era_str += "元"
            else:
                era_str += str(year - 1120 + 1)
            era_str += "年"
        elif year >= 1118:
            era_str += "元永"
            if year == 1118:
                era_str += "元"
            else:
                era_str += str(year - 1118 + 1)
            era_str += "年"
        elif year >= 1113:
            era_str += "永久"
            if year == 1113:
                era_str += "元"
            else:
                era_str += str(year - 1113 + 1)
            era_str += "年"
        elif year >= 1110:
            era_str += "天永"
            if year == 1110:
                era_str += "元"
            else:
                era_str += str(year - 1110 + 1)
            era_str += "年"
        elif year >= 1108:
            era_str += "天仁"
            if year == 1108:
                era_str += "元"
            else:
                era_str += str(year - 1108 + 1)
            era_str += "年"
        elif year >= 1106:
            era_str += "嘉承"
            if year == 1106:
                era_str += "元"
            else:
                era_str += str(year - 1106 + 1)
            era_str += "年"
        elif year >= 1104:
            era_str += "長治"
            if year == 1104:
                era_str += "元"
            else:
                era_str += str(year - 1104 + 1)
            era_str += "年"
        elif year >= 1099:
            era_str += "康和"
            if year == 1099:
                era_str += "元"
            else:
                era_str += str(year - 1099 + 1)
            era_str += "年"
        elif year >= 1097:
            era_str += "永長・承徳"
            if year == 1097:
                era_str += "元"
            else:
                era_str += str(year - 1097 + 1)
            era_str += "年"
        elif year >= 1095:
            era_str += "嘉保"
            if year == 1095:
                era_str += "元"
            else:
                era_str += str(year - 1095 + 1)
            era_str += "年"
        elif year >= 1087:
            era_str += "寛治"
            if year == 1087:
                era_str += "元"
            else:
                era_str += str(year - 1087 + 1)
            era_str += "年"
        elif year >= 1084:
            era_str += "応徳"
            if year == 1084:
                era_str += "元"
            else:
                era_str += str(year - 1084 + 1)
            era_str += "年"
        elif year >= 1081:
            era_str += "永保"
            if year == 1081:
                era_str += "元"
            else:
                era_str += str(year - 1081 + 1)
            era_str += "年"
        elif year >= 1077:
            era_str += "承暦"
            if year == 1077:
                era_str += "元"
            else:
                era_str += str(year - 1077 + 1)
            era_str += "年"
        elif year >= 1074:
            era_str += "承保"
            if year == 1074:
                era_str += "元"
            else:
                era_str += str(year - 1074 + 1)
            era_str += "年"
        elif year >= 1069:
            era_str += "延久"
            if year == 1069:
                era_str += "元"
            else:
                era_str += str(year - 1069 + 1)
            era_str += "年"
        elif year >= 1065:
            era_str += "治暦"
            if year == 1065:
                era_str += "元"
            else:
                era_str += str(year - 1065 + 1)
            era_str += "年"
        elif year >= 1058:
            era_str += "康平"
            if year == 1058:
                era_str += "元"
            else:
                era_str += str(year - 1058 + 1)
            era_str += "年"
        elif year >= 1053:
            era_str += "天喜"
            if year == 1053:
                era_str += "元"
            else:
                era_str += str(year - 1053 + 1)
            era_str += "年"
        elif year >= 1046:
            era_str += "永承"
            if year == 1046:
                era_str += "元"
            else:
                era_str += str(year - 1046 + 1)
            era_str += "年"
        elif year >= 1044:
            era_str += "寛徳"
            if year == 1044:
                era_str += "元"
            else:
                era_str += str(year - 1044 + 1)
            era_str += "年"
        elif year >= 1040:
            era_str += "長久"
            if year == 1040:
                era_str += "元"
            else:
                era_str += str(year - 1040 + 1)
            era_str += "年"
        elif year >= 1037:
            era_str += "長暦"
            if year == 1037:
                era_str += "元"
            else:
                era_str += str(year - 1037 + 1)
            era_str += "年"
        elif year >= 1028:
            era_str += "長元"
            if year == 1028:
                era_str += "元"
            else:
                era_str += str(year - 1028 + 1)
            era_str += "年"
        elif year >= 1024:
            era_str += "万寿"
            if year == 1024:
                era_str += "元"
            else:
                era_str += str(year - 1024 + 1)
            era_str += "年"
        elif year >= 1024:
            era_str += "万寿"
            if year == 1024:
                era_str += "元"
            else:
                era_str += str(year - 1024 + 1)
            era_str += "年"
        elif year >= 1021:
            era_str += "治安"
            if year == 1021:
                era_str += "元"
            else:
                era_str += str(year - 1021 + 1)
            era_str += "年"
        elif year >= 1017:
            era_str += "寛仁"
            if year == 1017:
                era_str += "元"
            else:
                era_str += str(year - 1017 + 1)
            era_str += "年"
        elif year >= 1013:
            era_str += "長和"
            if year == 1013:
                era_str += "元"
            else:
                era_str += str(year - 1013 + 1)
            era_str += "年"
        elif year >= 1004:
            era_str += "寛弘"
            if year == 1004:
                era_str += "元"
            else:
                era_str += str(year - 1004 + 1)
            era_str += "年"
        elif year >= 999:
            era_str += "長保"
            if year == 999:
                era_str += "元"
            else:
                era_str += str(year - 999 + 1)
            era_str += "年"
        elif year >= 995:
            era_str += "長徳"
            if year == 995:
                era_str += "元"
            else:
                era_str += str(year - 995 + 1)
            era_str += "年"
        elif year >= 990:
            era_str += "正暦"
            if year == 990:
                era_str += "元"
            else:
                era_str += str(year - 990 + 1)
            era_str += "年"
        elif year >= 987:
            era_str += "永延"
            if year == 987:
                era_str += "元"
            else:
                era_str += str(year - 987 + 1)
            era_str += "年"
        elif year >= 985:
            era_str += "寛和"
            if year == 985:
                era_str += "元"
            else:
                era_str += str(year - 985 + 1)
            era_str += "年"
        elif year >= 983:
            era_str += "永観"
            if year == 983:
                era_str += "元"
            else:
                era_str += str(year - 983 + 1)
            era_str += "年"
        elif year >= 978:
            era_str += "天元"
            if year == 978:
                era_str += "元"
            else:
                era_str += str(year - 978 + 1)
            era_str += "年"
        elif year >= 976:
            era_str += "貞元"
            if year == 976:
                era_str += "元"
            else:
                era_str += str(year - 976 + 1)
            era_str += "年"
        elif year >= 974:
            era_str += "天延"
            if year == 974:
                era_str += "元"
            else:
                era_str += str(year - 974 + 1)
            era_str += "年"
        elif year >= 970:
            era_str += "天禄"
            if year == 970:
                era_str += "元"
            else:
                era_str += str(year - 970 + 1)
            era_str += "年"
        elif year >= 968:
            era_str += "安和"
            if year == 968:
                era_str += "元"
            else:
                era_str += str(year - 968 + 1)
            era_str += "年"
        elif year >= 964:
            era_str += "康保"
            if year == 964:
                era_str += "元"
            else:
                era_str += str(year - 964 + 1)
            era_str += "年"
        elif year >= 961:
            era_str += "応和"
            if year == 961:
                era_str += "元"
            else:
                era_str += str(year - 961 + 1)
            era_str += "年"
        elif year >= 957:
            era_str += "天徳"
            if year == 957:
                era_str += "元"
            else:
                era_str += str(year - 957 + 1)
            era_str += "年"
        elif year >= 947:
            era_str += "天暦"
            if year == 947:
                era_str += "元"
            else:
                era_str += str(year - 947 + 1)
            era_str += "年"
        elif year >= 938:
            era_str += "天慶"
            if year == 938:
                era_str += "元"
            else:
                era_str += str(year - 938 + 1)
            era_str += "年"
        elif year >= 931:
            era_str += "承平"
            if year == 931:
                era_str += "元"
            else:
                era_str += str(year - 931 + 1)
            era_str += "年"
        elif year >= 923:
            era_str += "延長"
            if year == 923:
                era_str += "元"
            else:
                era_str += str(year - 923 + 1)
            era_str += "年"
        elif year >= 901:
            era_str += "延喜"
            if year == 901:
                era_str += "元"
            else:
                era_str += str(year - 901 + 1)
            era_str += "年"
        elif year >= 898:
            era_str += "昌泰"
            if year == 898:
                era_str += "元"
            else:
                era_str += str(year - 898 + 1)
            era_str += "年"
        elif year >= 889:
            era_str += "寛平"
            if year == 889:
                era_str += "元"
            else:
                era_str += str(year - 889 + 1)
            era_str += "年"
        elif year >= 885:
            era_str += "仁和"
            if year == 885:
                era_str += "元"
            else:
                era_str += str(year - 885 + 1)
            era_str += "年"
        elif year >= 877:
            era_str += "元慶"
            if year == 877:
                era_str += "元"
            else:
                era_str += str(year - 877 + 1)
            era_str += "年"
        elif year >= 859:
            era_str += "貞観"
            if year == 859:
                era_str += "元"
            else:
                era_str += str(year - 859 + 1)
            era_str += "年"
        elif year >= 857:
            era_str += "天安"
            if year == 857:
                era_str += "元"
            else:
                era_str += str(year - 857 + 1)
            era_str += "年"
        elif year >= 854:
            era_str += "斉衡"
            if year == 854:
                era_str += "元"
            else:
                era_str += str(year - 854 + 1)
            era_str += "年"
        elif year >= 851:
            era_str += "仁寿"
            if year == 851:
                era_str += "元"
            else:
                era_str += str(year - 851 + 1)
            era_str += "年"
        elif year >= 848:
            era_str += "嘉祥"
            if year == 848:
                era_str += "元"
            else:
                era_str += str(year - 848 + 1)
            era_str += "年"
        elif year >= 834:
            era_str += "承和"
            if year == 834:
                era_str += "元"
            else:
                era_str += str(year - 834 + 1)
            era_str += "年"
        elif year >= 824:
            era_str += "天長"
            if year == 824:
                era_str += "元"
            else:
                era_str += str(year - 824 + 1)
            era_str += "年"
        elif year >= 810:
            era_str += "弘仁"
            if year == 810:
                era_str += "元"
            else:
                era_str += str(year - 810 + 1)
            era_str += "年"
        elif year >= 806:
            era_str += "大同"
            if year == 806:
                era_str += "元"
            else:
                era_str += str(year - 806 + 1)
            era_str += "年"
        elif year >= 782:
            era_str += "延暦"
            if year == 782:
                era_str += "元"
            else:
                era_str += str(year - 782 + 1)
            era_str += "年"
    elif year >= 710:
        era_str += "奈良時代/"
        if year >= 782:
            era_str += "延暦"
            if year == 782:
                era_str += "元"
            else:
                era_str += str(year - 782 + 1)
            era_str += "年"
        elif year >= 781:
            era_str += "天応"
            if year == 781:
                era_str += "元"
            else:
                era_str += str(year - 781 + 1)
            era_str += "年"
        elif year >= 770:
            era_str += "宝亀"
            if year == 770:
                era_str += "元"
            else:
                era_str += str(year - 770 + 1)
            era_str += "年"
        elif year >= 767:
            era_str += "神護景雲"
            if year == 767:
                era_str += "元"
            else:
                era_str += str(year - 767 + 1)
            era_str += "年"
        elif year >= 765:
            era_str += "天平神護"
            if year == 765:
                era_str += "元"
            else:
                era_str += str(year - 765 + 1)
            era_str += "年"
        elif year >= 757:
            era_str += "天平宝字"
            if year == 757:
                era_str += "元"
            else:
                era_str += str(year - 757 + 1)
            era_str += "年"
        elif year >= 749:
            era_str += "天平勝宝"
            if year == 749:
                era_str += "元"
            else:
                era_str += str(year - 749 + 1)
            era_str += "年"
        elif year >= 729:
            era_str += "天平"
            if year == 729:
                era_str += "元"
            else:
                era_str += str(year - 729 + 1)
            era_str += "年"
        elif year >= 724:
            era_str += "神亀"
            if year == 724:
                era_str += "元"
            else:
                era_str += str(year - 724 + 1)
            era_str += "年"
        elif year >= 717:
            era_str += "養老"
            if year == 717:
                era_str += "元"
            else:
                era_str += str(year - 717 + 1)
            era_str += "年"
        elif year >= 715:
            era_str += "霊亀"
            if year == 715:
                era_str += "元"
            else:
                era_str += str(year - 715 + 1)
            era_str += "年"
        elif year >= 708:
            era_str += "和銅"
            if year == 708:
                era_str += "元"
            else:
                era_str += str(year - 708 + 1)
            era_str += "年"
    elif year >= 645:
        era_str += "飛鳥時代/"
        if year >= 708:
            era_str += "和銅"
            if year == 708:
                era_str += "元"
            else:
                era_str += str(year - 708 + 1)
            era_str += "年"
        elif year >= 704:
            era_str += "慶雲"
            if year == 704:
                era_str += "元"
            else:
                era_str += str(year - 704 + 1)
            era_str += "年"
        elif year >= 701:
            era_str += "大宝"
            if year == 701:
                era_str += "元"
            else:
                era_str += str(year - 701 + 1)
            era_str += "年"
        elif year >= 686:
            era_str += "朱鳥・元号なし"
            if year == 686:
                era_str += "元"
            else:
                era_str += str(year - 686 + 1)
            era_str += "年"
    return era_str



def calendar(year,color):
    jp_zodiac       = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
    jp_zodiac_jruby = ["ねずみ（ね）","うし","とら","うさぎ（う）","たつ","へび（み）","うま","ひつじ","さる","とり","いぬ","いのしし（い）"]
    jp_zodiac_eruby = ["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","cock","dog","boar"]
    month_date      = [31,28+leap(year),31,30,31,30,31,31,30,31,30,31]
    month_name      = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    month_jpname    = ["睦月","如月","弥生","卯月","皐月","水無月","文月","葉月","長月","神無月","霜月","師走"]



    cale_str = ""
    for month in range(1,13):
        count = ZellersCongruence(year,month,1)
        cale_str += "\\begin{center}\n"
        cale_str += "\t\\HUGE " + str(year) + "年\\\\\n"
        cale_str += "\t\\huge " + str(month) + "月\\\\\n"
        cale_str += "\t\\large "

        cale_str += eraname(year)

        cale_str += "(" + jp_zodiac[(year%12)-4] + "年[" + jp_zodiac_jruby[(year%12)-4]  + "," + jp_zodiac_eruby[(year%12)-4] + "])"

        cale_str += month_name[month-1] + "(" + month_jpname[month-1] + ")\n"
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
    str += "\\usepackage[top=2cm , bottom = 1cm , left = 2cm , right = 2cm , includefoot]{geometry}\n"
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
