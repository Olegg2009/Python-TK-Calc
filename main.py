import tkinter as tk
import math

countText = ""
historyText = ""
acts = ""
nums = []
res = ()


def one():
    global countText
    countText += "1"
    lbl.configure(text=countText)


def two():
    global countText
    countText += "2"
    lbl.configure(text=countText)


def three():
    global countText
    countText += "3"
    lbl.configure(text=countText)


def four():
    global countText
    countText += "4"
    lbl.configure(text=countText)


def five():
    global countText
    countText += "5"
    lbl.configure(text=countText)


def six():
    global countText
    countText += "6"
    lbl.configure(text=countText)


def seven():
    global countText
    countText += "7"
    lbl.configure(text=countText)


def eight():
    global countText
    countText += "8"
    lbl.configure(text=countText)


def nine():
    global countText
    countText += "9"
    lbl.configure(text=countText)


def zero():
    global countText
    countText += "0"
    if len(countText) == 1:
        countText += "."
    lbl.configure(text=countText)


def plus():
    global nums
    global countText
    global acts
    global historyText
    historyText += f'{lbl.cget("text")} + '
    hist.configure(text=historyText)
    nums.append(float(lbl.cget("text")))
    lbl.configure(text="0")
    countText = ""
    acts += "+"


def minus():
    global nums
    global countText
    global acts
    global historyText
    historyText += f'{lbl.cget("text")} - '
    hist.configure(text=historyText)
    nums.append(float(lbl.cget("text")))
    lbl.configure(text="0")
    countText = ""
    acts += "-"


def mult():
    global nums
    global countText
    global acts
    global historyText
    historyText += f'{lbl.cget("text")} x '
    hist.configure(text=historyText)
    nums.append(float(lbl.cget("text")))
    lbl.configure(text="0")
    countText = ""
    acts += "*"


def dis():
    global nums
    global countText
    global acts
    global historyText
    historyText += f'{lbl.cget("text")} : '
    hist.configure(text=historyText)
    nums.append(float(lbl.cget("text")))
    lbl.configure(text="0")
    countText = ""
    acts += "/"


def exp():
    global nums
    global countText
    global acts
    global historyText
    historyText += f'{lbl.cget("text")} ^ '
    hist.configure(text=historyText)
    nums.append(float(lbl.cget("text")))
    lbl.configure(text="0")
    countText = ""
    acts += "^"


def sqr():
    global nums
    global countText
    global acts
    global historyText
    historyText += f'{lbl.cget("text")} √'
    hist.configure(text=historyText)
    nums.append(float(lbl.cget("text")))
    lbl.configure(text="0")
    countText = ""
    acts += "√"


def resul():
    global nums
    global countText
    global acts
    global res
    global historyText
    historyText += f'{lbl.cget("text")} = '
    nums.append(float(lbl.cget("text")))
    print(nums)
    for i in range(len(nums) - 1):
        print(acts)
        if "^" in acts or ("^" in acts and "√" in acts and acts.index("^") > acts.index("√")):
            local = nums[acts.index("^")] ** nums[acts.index("^") + 1]
            nums[acts.index("^") + 1] = local
            nums.pop(acts.index("^"))
            acts = acts.replace("^", "", 1)
            print(acts)
        elif "√" in acts:
            nums[acts.index("√") + 1] = math.sqrt(nums[acts.index("√") + 1])
            nums.pop(acts.index("√"))
            acts = acts.replace("√", "", 1)
        elif "*" in acts or ("*" in acts and "/" in acts and acts.index("*") > acts.index("/")):
            local = nums[acts.index("*")] * nums[acts.index("*") + 1]
            nums[acts.index("*") + 1] = local
            nums.pop(acts.index("*"))
            acts = acts.replace("*", "", 1)
            print(acts)
        elif "/" in acts:
            if nums[(acts.index("/")) + 1] == 0 or 0.:
                window.quit()
            else:
                local = nums[acts.index("/")] / nums[acts.index("/") + 1]
                nums[acts.index("/") + 1] = local
                nums.pop(acts.index("/"))
                acts = acts.replace("/", "", 1)
                print(acts)
        elif "+" in acts or ("+" in acts and "-" in acts and acts.index("+") > acts.index("-")):
            local = nums[acts.index("+")] + nums[acts.index("+") + 1]
            nums[acts.index("+") + 1] = local
            nums.pop(acts.index("+"))
            acts = acts.replace("+", "", 1)
            print(acts)
        elif "-" in acts:
            local = nums[acts.index("-")] - nums[acts.index("-") + 1]
            nums[acts.index("-") + 1] = local
            nums.pop(acts.index("-"))
            acts = acts.replace("-", "", 1)
            print(acts)
    print(nums)
    res = round(nums[0], 1)
    acts = ""
    lbl.configure(text=res)
    countText = str(lbl.cget("text"))
    historyText += str(res)
    hist.configure(text=historyText)
    historyText = ""
    nums = []


def C():
    global countText
    countText = ""
    lbl.configure(text="0")


def PM():
    global countText
    if countText != "":
        if countText[0] != "-":
            countText = "-" + countText
        else:
            countText = countText.replace("-", "", 1)
        lbl.configure(text=countText)


def dot():
    global countText
    if countText != "" and "." not in countText:
        countText = countText + "."
        lbl.configure(text=countText)


bg = '#696969'

window = tk.Tk()
window.title("Калькулятор")
window.geometry('+260+390')
window.resizable(width=False, height=False)
window.configure(background="#404040")

hist = tk.Label(window, text="0", bg="#696969", font=("Arial", 8))
hist.grid(row=0, column=0)

lbl = tk.Label(window, text="0", relief=tk.SUNKEN, borderwidth=1, bg=bg, font=("Arial", 30))
lbl.grid(row=1, column=0)

clav = tk.Frame()
clav.grid(row=2, column=0)

btn1 = tk.Button(clav, text="1", width=5, height=3, command=one, bg=bg, font="Arial", )
btn1.grid(row=1, column=1)

btn2 = tk.Button(clav, text="2", width=5, height=3, command=two, bg=bg, font="Arial")
btn2.grid(row=1, column=2)

btn3 = tk.Button(clav, text="3", width=5, height=3, command=three, bg=bg, font="Arial")
btn3.grid(row=1, column=3)

btn4 = tk.Button(clav, text="4", width=5, height=3, command=four, bg=bg, font="Arial")
btn4.grid(row=2, column=1)

btn5 = tk.Button(clav, text="5", width=5, height=3, command=five, bg=bg, font="Arial")
btn5.grid(row=2, column=2)

btn6 = tk.Button(clav, text="6", width=5, height=3, command=six, bg=bg, font="Arial")
btn6.grid(row=2, column=3)

btn7 = tk.Button(clav, text="7", width=5, height=3, command=seven, bg=bg, font="Arial")
btn7.grid(row=3, column=1)

btn8 = tk.Button(clav, text="8", width=5, height=3, command=eight, bg=bg, font="Arial")
btn8.grid(row=3, column=2)

btn9 = tk.Button(clav, text="9", width=5, height=3, command=nine, bg=bg, font="Arial")
btn9.grid(row=3, column=3)

btn0 = tk.Button(clav, text="0", width=5, height=3, command=zero, bg=bg, font="Arial")
btn0.grid(row=4, column=2)

btnPlus = tk.Button(clav, text="+", width=5, height=3, command=plus, bg=bg, font="Arial")
btnPlus.grid(row=1, column=4)

btnMinus = tk.Button(clav, text="-", width=5, height=3, command=minus, bg=bg, font="Arial")
btnMinus.grid(row=2, column=4)

btnMult = tk.Button(clav, text="x", width=5, height=3, command=mult, bg=bg, font="Arial")
btnMult.grid(row=3, column=4)

btnDis = tk.Button(clav, text=":", width=5, height=3, command=dis, bg=bg, font="Arial")
btnDis.grid(row=4, column=4)

btnRes = tk.Button(clav, text="=", width=5, height=3, command=resul, bg=bg, font="Arial")
btnRes.grid(row=4, column=3)

btnC = tk.Button(clav, text="C", width=5, height=3, command=C, bg=bg, font="Arial")
btnC.grid(row=4, column=1)

btnExp = tk.Button(clav, text="^", width=5, height=3, command=exp, bg=bg, font="Arial")
btnExp.grid(row=1, column=5)

btnExp = tk.Button(clav, text="√", width=5, height=3, command=sqr, bg=bg, font="Arial")
btnExp.grid(row=2, column=5)

btnPM = tk.Button(clav, text="-/+", width=5, height=3, command=PM, bg=bg, font="Arial")
btnPM.grid(row=3, column=5)

btnPM = tk.Button(clav, text=",", width=5, height=3, command=dot, bg=bg, font="Arial")
btnPM.grid(row=4, column=5)

window.mainloop()
