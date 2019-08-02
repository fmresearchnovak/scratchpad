#!/usr/bin/env python3

import tkinter
import re # python regular expression module

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.



class Pad():
	def __init__(self):

		self.resetting_modified_flag = False
		#print("flag: " + str(self.resetting_modified_flag))

		root = tkinter.Tk()
		root.title("Scratchpad")


		self.padding = 15
		self.text_ed = tkinter.Text(root, width=50, height=30, bg = "#ffffff", borderwidth=0, highlightthickness=0, padx=self.padding, pady=self.padding)
		self.text_ed.pack(side=tkinter.LEFT)

		self.text_out = tkinter.Text(root, width=25, height=30, bg = "#c8c8c8", padx=self.padding, pady=self.padding)
		self.text_out.config(state=tkinter.DISABLED)
		self.text_out.pack(side=tkinter.RIGHT)


		self.text_ed.bind("<<Modified>>", self.onModified)

		tkinter.mainloop()


	def onModified(self, event):

		if(self.resetting_modified_flag): 
			self.resetting_modified_flag = False
			return


		input_text = self.text_ed.get("1.0",'end-1c')
		#print("printing input text: " + str(input_text))


		self.text_out.config(state=tkinter.NORMAL)
		self.text_out.delete("1.0", tkinter.END)
		regexparse = r'\d+|[+/*-==()]'

		print("\n")
		for line in input_text.split("\n"):
			print("line: " + str(line))
			line = line.replace(":", "")



			# Try regex to match math equations
			elem = re.findall(regexparse, line)
			elem = "".join(elem).encode('ascii','ignore')
			print("found math: " + str(elem))

			try:
				ans = eval(elem)
				print("\tevaluated to: " + str(ans))
				self.text_out.insert(tkinter.INSERT, str(ans) + "\n")

			except SyntaxError as se:
				print("\t" + str(se))
				print("\tfailed to evaluate!")
				self.text_out.insert(tkinter.INSERT, "\n")


		self.text_out.config(state=tkinter.DISABLED)
		self.resetting_modified_flag = True
		res = self.text_ed.edit_modified(0)




if __name__ == "__main__":
	p = Pad()

