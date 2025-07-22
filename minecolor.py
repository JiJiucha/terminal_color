import color


def minecolor(t:str):
	result=''
	index=0
	while True:
		if (index>=len(t)):
			return result
		string=t[index]
		#print(result,index,string,len(t),index>=len(t))
		if string=='§':
			if not (index+1>=len(t)):
				control=t[index+1]
				if control=='0':
					result+=color.text_color_rgb(0,0,0)
				if control=='1':
					result+=color.text_color_rgb(0,0,170)
				if control=='2':
					result+=color.text_color_rgb(0,170,0)
				if control=='3':
					result+=color.text_color_rgb(0,170,170)
				if control=='4':
					result+=color.text_color_rgb(170,0,0)
				if control=='5':
					result+=color.text_color_rgb(170,0,170)
				if control=='6':
					result+=color.text_color_rgb(255,170,0)
				if control=='7':
					result+=color.text_color_rgb(170,170,170)
				if control=='8':
					result+=color.text_color_rgb(85,85,85)
				if control=='9':
					result+=color.text_color_rgb(85,85,255)
				if control=='a':
					result+=color.text_color_rgb(85,255,85)
				if control=='b':
					result+=color.text_color_rgb(85,255,255)
				if control=='c':
					result+=color.text_color_rgb(255,85,85)
				if control=='d':
					result+=color.text_color_rgb(255,85,255)
				if control=='e':
					result+=color.text_color_rgb(255,255,85)
				if control=='f':
					result+=color.text_color_rgb(255,255,255)
				if control=='g':
					result+=color.text_color_rgb(221,214,5)
				if control=='l':
					result+=color.string_style('bright')
				if control=='r':
					result+=color.reset_all()
				index+=1
		else:
			result+=string
		index+=1
