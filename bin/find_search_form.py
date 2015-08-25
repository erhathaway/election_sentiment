import mechanize


browserSpecs = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-Agent', browserSpecs), ('Accept', '*/*')] # need ths to re-direct

# SEARCH A SITE FOR FORMS AND FORM CONTROLS----------------------------------------------------------------------
def find_search(site):
  br.open(site)
  index = 0
  for form in br.forms():
      print "----------FORM----------------------"
      print "Form name:", form.name, "Form index:", index
      # print form
      # print
      index +=1
      subindex = 0
      for control in form.controls:
        print "---------->>CONTROL----------------------"
        print "control name:", control.name, "control_index", index
        print "control type:", control.type
        subindex +=1