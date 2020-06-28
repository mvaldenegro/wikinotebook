# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Wed Mar 20 00:13:21 2019
#      by: The Resource Compiler for PySide2 (Qt v5.12.1)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x01\xdd\
#\
# WebEngine Mark\
down Editor Exam\
ple\x0a\x0aThis exampl\
e uses [QWebEngi\
neView](http://d\
oc.qt.io/qt-5/qw\
ebengineview.htm\
l)\x0ato preview te\
xt written using\
 the [Markdown](\
https://en.wikip\
edia.org/wiki/Ma\
rkdown)\x0asyntax.\x0a\
\x0a### Acknowledgm\
ents\x0a\x0aThe conver\
sion from Markdo\
wn to HTML is do\
ne with the help\
 of the\x0a[marked \
JavaScript libra\
ry](https://gith\
ub.com/chjj/mark\
ed) by _Christop\
her Jeffrey_.\x0aTh\
e [style sheet](\
https://kevinbur\
ke.bitbucket.io/\
markdowncss/)\x0awa\
s created by _Ke\
vin Burke_.\x0a\
\x00\x00\x02\xbc\
<\
!doctype html>\x0a<\
html lang=\x22en\x22>\x0a\
<meta charset=\x22u\
tf-8\x22>\x0a<head>\x0a  \
<link rel=\x22style\
sheet\x22 type=\x22tex\
t/css\x22 href=\x22qrc\
:/3rdparty/markd\
own.css\x22>\x0a  <scr\
ipt src=\x22qrc:/3r\
dparty/marked.js\
\x22></script>\x0a  <s\
cript src=\x22qrc:/\
qtwebchannel/qwe\
bchannel.js\x22></s\
cript>\x0a</head>\x0a<\
body>\x0a  <div id=\
\x22placeholder\x22></\
div>\x0a  <script>\x0a\
  'use strict';\x0a\
\x0a  var placehold\
er = document.ge\
tElementById('pl\
aceholder');\x0a\x0a  \
var updateText =\
 function(text) \
{\x0a      placehol\
der.innerHTML = \
marked(text);\x0a  \
}\x0a\x0a  new QWebCha\
nnel(qt.webChann\
elTransport,\x0a   \
 function(channe\
l) {\x0a      var c\
ontent = channel\
.objects.content\
;\x0a      updateTe\
xt(content.text)\
;\x0a      content.\
textChanged.conn\
ect(updateText);\
\x0a    }\x0a  );\x0a  </\
script>\x0a</body>\x0a\
</html>\x0a\x0a\x0a\x0a\
\x00\x00\x17e\
b\
ody{\x0a    margin:\
 0 auto;\x0a    fon\
t-family: Georgi\
a, Palatino, ser\
if;\x0a    color: #\
444444;\x0a    line\
-height: 1;\x0a    \
max-width: 960px\
;\x0a    padding: 3\
0px;\x0a}\x0ah1, h2, h\
3, h4 {\x0a    colo\
r: #111111;\x0a    \
font-weight: 400\
;\x0a}\x0ah1, h2, h3, \
h4, h5, p {\x0a    \
margin-bottom: 2\
4px;\x0a    padding\
: 0;\x0a}\x0ah1 {\x0a    \
font-size: 48px;\
\x0a}\x0ah2 {\x0a    font\
-size: 36px;\x0a   \
 /* The bottom m\
argin is small. \
It's designed to\
 be used with gr\
ay meta text\x0a   \
  * below a post\
 title. */\x0a    m\
argin: 24px 0 6p\
x;\x0a}\x0ah3 {\x0a    fo\
nt-size: 24px;\x0a}\
\x0ah4 {\x0a    font-s\
ize: 21px;\x0a}\x0ah5 \
{\x0a    font-size:\
 18px;\x0a}\x0aa {\x0a   \
 color: #0099ff;\
\x0a    margin: 0;\x0a\
    padding: 0;\x0a\
    vertical-ali\
gn: baseline;\x0a}\x0a\
a:hover {\x0a    te\
xt-decoration: n\
one;\x0a    color: \
#ff6600;\x0a}\x0aa:vis\
ited {\x0a    color\
: purple;\x0a}\x0aul, \
ol {\x0a    padding\
: 0;\x0a    margin:\
 0;\x0a}\x0ali {\x0a    l\
ine-height: 24px\
;\x0a}\x0ali ul, li ul\
 {\x0a    margin-le\
ft: 24px;\x0a}\x0ap, u\
l, ol {\x0a    font\
-size: 16px;\x0a   \
 line-height: 24\
px;\x0a    max-widt\
h: 540px;\x0a}\x0apre \
{\x0a    padding: 0\
px 24px;\x0a    max\
-width: 800px;\x0a \
   white-space: \
pre-wrap;\x0a}\x0acode\
 {\x0a    font-fami\
ly: Consolas, Mo\
naco, Andale Mon\
o, monospace;\x0a  \
  line-height: 1\
.5;\x0a    font-siz\
e: 13px;\x0a}\x0aaside\
 {\x0a    display: \
block;\x0a    float\
: right;\x0a    wid\
th: 390px;\x0a}\x0ablo\
ckquote {\x0a    bo\
rder-left:.5em s\
olid #eee;\x0a    p\
adding: 0 2em;\x0a \
   margin-left:0\
;\x0a    max-width:\
 476px;\x0a}\x0ablockq\
uote  cite {\x0a   \
 font-size:14px;\
\x0a    line-height\
:20px;\x0a    color\
:#bfbfbf;\x0a}\x0abloc\
kquote cite:befo\
re {\x0a    content\
: '\x5c2014 \x5c00A0';\
\x0a}\x0a\x0ablockquote p\
 {\x0a    color: #6\
66;\x0a    max-widt\
h: 460px;\x0a}\x0ahr {\
\x0a    width: 540p\
x;\x0a    text-alig\
n: left;\x0a    mar\
gin: 0 auto 0 0;\
\x0a    color: #999\
;\x0a}\x0a\x0a/* Code bel\
ow this line is \
copyright Twitte\
r Inc. */\x0a\x0abutto\
n,\x0ainput,\x0aselect\
,\x0atextarea {\x0a  f\
ont-size: 100%;\x0a\
  margin: 0;\x0a  v\
ertical-align: b\
aseline;\x0a  *vert\
ical-align: midd\
le;\x0a}\x0abutton, in\
put {\x0a  line-hei\
ght: normal;\x0a  *\
overflow: visibl\
e;\x0a}\x0abutton::-mo\
z-focus-inner, i\
nput::-moz-focus\
-inner {\x0a  borde\
r: 0;\x0a  padding:\
 0;\x0a}\x0abutton,\x0ain\
put[type=\x22button\
\x22],\x0ainput[type=\x22\
reset\x22],\x0ainput[t\
ype=\x22submit\x22] {\x0a\
  cursor: pointe\
r;\x0a  -webkit-app\
earance: button;\
\x0a}\x0ainput[type=ch\
eckbox], input[t\
ype=radio] {\x0a  c\
ursor: pointer;\x0a\
}\x0a/* override de\
fault chrome & f\
irefox settings \
*/\x0ainput:not([ty\
pe=\x22image\x22]), te\
xtarea {\x0a  -webk\
it-box-sizing: c\
ontent-box;\x0a  -m\
oz-box-sizing: c\
ontent-box;\x0a  bo\
x-sizing: conten\
t-box;\x0a}\x0a\x0ainput[\
type=\x22search\x22] {\
\x0a  -webkit-appea\
rance: textfield\
;\x0a  -webkit-box-\
sizing: content-\
box;\x0a  -moz-box-\
sizing: content-\
box;\x0a  box-sizin\
g: content-box;\x0a\
}\x0ainput[type=\x22se\
arch\x22]::-webkit-\
search-decoratio\
n {\x0a  -webkit-ap\
pearance: none;\x0a\
}\x0alabel,\x0ainput,\x0a\
select,\x0atextarea\
 {\x0a  font-family\
: \x22Helvetica Neu\
e\x22, Helvetica, A\
rial, sans-serif\
;\x0a  font-size: 1\
3px;\x0a  font-weig\
ht: normal;\x0a  li\
ne-height: norma\
l;\x0a  margin-bott\
om: 18px;\x0a}\x0ainpu\
t[type=checkbox]\
, input[type=rad\
io] {\x0a  cursor: \
pointer;\x0a  margi\
n-bottom: 0;\x0a}\x0ai\
nput[type=text],\
\x0ainput[type=pass\
word],\x0atextarea,\
\x0aselect {\x0a  disp\
lay: inline-bloc\
k;\x0a  width: 210p\
x;\x0a  padding: 4p\
x;\x0a  font-size: \
13px;\x0a  font-wei\
ght: normal;\x0a  l\
ine-height: 18px\
;\x0a  height: 18px\
;\x0a  color: #8080\
80;\x0a  border: 1p\
x solid #ccc;\x0a  \
-webkit-border-r\
adius: 3px;\x0a  -m\
oz-border-radius\
: 3px;\x0a  border-\
radius: 3px;\x0a}\x0as\
elect, input[typ\
e=file] {\x0a  heig\
ht: 27px;\x0a  line\
-height: 27px;\x0a}\
\x0atextarea {\x0a  he\
ight: auto;\x0a}\x0a\x0a/\
* grey out place\
holders */\x0a:-moz\
-placeholder {\x0a \
 color: #bfbfbf;\
\x0a}\x0a::-webkit-inp\
ut-placeholder {\
\x0a  color: #bfbfb\
f;\x0a}\x0a\x0ainput[type\
=text],\x0ainput[ty\
pe=password],\x0ase\
lect,\x0atextarea {\
\x0a  -webkit-trans\
ition: border li\
near 0.2s, box-s\
hadow linear 0.2\
s;\x0a  -moz-transi\
tion: border lin\
ear 0.2s, box-sh\
adow linear 0.2s\
;\x0a  transition: \
border linear 0.\
2s, box-shadow l\
inear 0.2s;\x0a  -w\
ebkit-box-shadow\
: inset 0 1px 3p\
x rgba(0, 0, 0, \
0.1);\x0a  -moz-box\
-shadow: inset 0\
 1px 3px rgba(0,\
 0, 0, 0.1);\x0a  b\
ox-shadow: inset\
 0 1px 3px rgba(\
0, 0, 0, 0.1);\x0a}\
\x0ainput[type=text\
]:focus, input[t\
ype=password]:fo\
cus, textarea:fo\
cus {\x0a  outline:\
 none;\x0a  border-\
color: rgba(82, \
168, 236, 0.8);\x0a\
  -webkit-box-sh\
adow: inset 0 1p\
x 3px rgba(0, 0,\
 0, 0.1), 0 0 8p\
x rgba(82, 168, \
236, 0.6);\x0a  -mo\
z-box-shadow: in\
set 0 1px 3px rg\
ba(0, 0, 0, 0.1)\
, 0 0 8px rgba(8\
2, 168, 236, 0.6\
);\x0a  box-shadow:\
 inset 0 1px 3px\
 rgba(0, 0, 0, 0\
.1), 0 0 8px rgb\
a(82, 168, 236, \
0.6);\x0a}\x0a\x0a/* butt\
ons */\x0abutton {\x0a\
  display: inlin\
e-block;\x0a  paddi\
ng: 4px 14px;\x0a  \
font-family: \x22He\
lvetica Neue\x22, H\
elvetica, Arial,\
 sans-serif;\x0a  f\
ont-size: 13px;\x0a\
  line-height: 1\
8px;\x0a  -webkit-b\
order-radius: 4p\
x;\x0a  -moz-border\
-radius: 4px;\x0a  \
border-radius: 4\
px;\x0a  -webkit-bo\
x-shadow: inset \
0 1px 0 rgba(255\
, 255, 255, 0.2)\
, 0 1px 2px rgba\
(0, 0, 0, 0.05);\
\x0a  -moz-box-shad\
ow: inset 0 1px \
0 rgba(255, 255,\
 255, 0.2), 0 1p\
x 2px rgba(0, 0,\
 0, 0.05);\x0a  box\
-shadow: inset 0\
 1px 0 rgba(255,\
 255, 255, 0.2),\
 0 1px 2px rgba(\
0, 0, 0, 0.05);\x0a\
  background-col\
or: #0064cd;\x0a  b\
ackground-repeat\
: repeat-x;\x0a  ba\
ckground-image: \
-khtml-gradient(\
linear, left top\
, left bottom, f\
rom(#049cdb), to\
(#0064cd));\x0a  ba\
ckground-image: \
-moz-linear-grad\
ient(top, #049cd\
b, #0064cd);\x0a  b\
ackground-image:\
 -ms-linear-grad\
ient(top, #049cd\
b, #0064cd);\x0a  b\
ackground-image:\
 -webkit-gradien\
t(linear, left t\
op, left bottom,\
 color-stop(0%, \
#049cdb), color-\
stop(100%, #0064\
cd));\x0a  backgrou\
nd-image: -webki\
t-linear-gradien\
t(top, #049cdb, \
#0064cd);\x0a  back\
ground-image: -o\
-linear-gradient\
(top, #049cdb, #\
0064cd);\x0a  backg\
round-image: lin\
ear-gradient(top\
, #049cdb, #0064\
cd);\x0a  color: #f\
ff;\x0a  text-shado\
w: 0 -1px 0 rgba\
(0, 0, 0, 0.25);\
\x0a  border: 1px s\
olid #004b9a;\x0a  \
border-bottom-co\
lor: #003f81;\x0a  \
-webkit-transiti\
on: 0.1s linear \
all;\x0a  -moz-tran\
sition: 0.1s lin\
ear all;\x0a  trans\
ition: 0.1s line\
ar all;\x0a  border\
-color: #0064cd \
#0064cd #003f81;\
\x0a  border-color:\
 rgba(0, 0, 0, 0\
.1) rgba(0, 0, 0\
, 0.1) rgba(0, 0\
, 0, 0.25);\x0a}\x0abu\
tton:hover {\x0a  c\
olor: #fff;\x0a  ba\
ckground-positio\
n: 0 -15px;\x0a  te\
xt-decoration: n\
one;\x0a}\x0abutton:ac\
tive {\x0a  -webkit\
-box-shadow: ins\
et 0 3px 7px rgb\
a(0, 0, 0, 0.15)\
, 0 1px 2px rgba\
(0, 0, 0, 0.05);\
\x0a  -moz-box-shad\
ow: inset 0 3px \
7px rgba(0, 0, 0\
, 0.15), 0 1px 2\
px rgba(0, 0, 0,\
 0.05);\x0a  box-sh\
adow: inset 0 3p\
x 7px rgba(0, 0,\
 0, 0.15), 0 1px\
 2px rgba(0, 0, \
0, 0.05);\x0a}\x0abutt\
on::-moz-focus-i\
nner {\x0a  padding\
: 0;\x0a  border: 0\
;\x0a}\x0a\
\x00\x00\x91D\
/\
**\x0a * marked - a\
 markdown parser\
\x0a * Copyright (c\
) 2011-2014, Chr\
istopher Jeffrey\
. (MIT Licensed)\
\x0a * https://gith\
ub.com/markedjs/\
marked\x0a */\x0a\x0a;(fu\
nction(root) {\x0a'\
use strict';\x0a\x0a/*\
*\x0a * Block-Level\
 Grammar\x0a */\x0a\x0ava\
r block = {\x0a  ne\
wline: /^\x5cn+/,\x0a \
 code: /^( {4}[^\
\x5cn]+\x5cn*)+/,\x0a  fe\
nces: noop,\x0a  hr\
: /^ {0,3}((?:- \
*){3,}|(?:_ *){3\
,}|(?:\x5c* *){3,})\
(?:\x5cn+|$)/,\x0a  he\
ading: /^ *(#{1,\
6}) *([^\x5cn]+?) *\
(?:#+ *)?(?:\x5cn+|\
$)/,\x0a  nptable: \
noop,\x0a  blockquo\
te: /^( {0,3}> ?\
(paragraph|[^\x5cn]\
*)(?:\x5cn|$))+/,\x0a \
 list: /^( *)(bu\
ll) [\x5cs\x5cS]+?(?:h\
r|def|\x5cn{2,}(?! \
)(?!\x5c1bull )\x5cn*|\
\x5cs*$)/,\x0a  html: \
'^ {0,3}(?:' // \
optional indenta\
tion\x0a    + '<(sc\
ript|pre|style)[\
\x5c\x5cs>][\x5c\x5cs\x5c\x5cS]*?(\
?:</\x5c\x5c1>[^\x5c\x5cn]*\x5c\
\x5cn+|$)' // (1)\x0a \
   + '|comment[^\
\x5c\x5cn]*(\x5c\x5cn+|$)' /\
/ (2)\x0a    + '|<\x5c\
\x5c?[\x5c\x5cs\x5c\x5cS]*?\x5c\x5c?>\
\x5c\x5cn*' // (3)\x0a   \
 + '|<![A-Z][\x5c\x5cs\
\x5c\x5cS]*?>\x5c\x5cn*' // \
(4)\x0a    + '|<!\x5c\x5c\
[CDATA\x5c\x5c[[\x5c\x5cs\x5c\x5cS\
]*?\x5c\x5c]\x5c\x5c]>\x5c\x5cn*' \
// (5)\x0a    + '|<\
/?(tag)(?: +|\x5c\x5cn\
|/?>)[\x5c\x5cs\x5c\x5cS]*?(\
?:\x5c\x5cn{2,}|$)' //\
 (6)\x0a    + '|<(?\
!script|pre|styl\
e)([a-z][\x5c\x5cw-]*)\
(?:attribute)*? \
*/?>(?=\x5c\x5ch*\x5c\x5cn)[\
\x5c\x5cs\x5c\x5cS]*?(?:\x5c\x5cn{\
2,}|$)' // (7) o\
pen tag\x0a    + '|\
</(?!script|pre|\
style)[a-z][\x5c\x5cw-\
]*\x5c\x5cs*>(?=\x5c\x5ch*\x5c\x5c\
n)[\x5c\x5cs\x5c\x5cS]*?(?:\x5c\
\x5cn{2,}|$)' // (7\
) closing tag\x0a  \
  + ')',\x0a  def: \
/^ {0,3}\x5c[(label\
)\x5c]: *\x5cn? *<?([^\
\x5cs>]+)>?(?:(?: +\
\x5cn? *| *\x5cn *)(ti\
tle))? *(?:\x5cn+|$\
)/,\x0a  table: noo\
p,\x0a  lheading: /\
^([^\x5cn]+)\x5cn *(=|\
-){2,} *(?:\x5cn+|$\
)/,\x0a  paragraph:\
 /^([^\x5cn]+(?:\x5cn(\
?!hr|heading|lhe\
ading| {0,3}>|<\x5c\
/?(?:tag)(?: +|\x5c\
n|\x5c/?>)|<(?:scri\
pt|pre|style|!--\
))[^\x5cn]+)*)/,\x0a  \
text: /^[^\x5cn]+/\x0a\
};\x0a\x0ablock._label\
 = /(?!\x5cs*\x5c])(?:\
\x5c\x5c[\x5c[\x5c]]|[^\x5c[\x5c]]\
)+/;\x0ablock._titl\
e = /(?:\x22(?:\x5c\x5c\x22?\
|[^\x22\x5c\x5c])*\x22|'[^'\x5c\
n]*(?:\x5cn[^'\x5cn]+)\
*\x5cn?'|\x5c([^()]*\x5c)\
)/;\x0ablock.def = \
edit(block.def)\x0a\
  .replace('labe\
l', block._label\
)\x0a  .replace('ti\
tle', block._tit\
le)\x0a  .getRegex(\
);\x0a\x0ablock.bullet\
 = /(?:[*+-]|\x5cd+\
\x5c.)/;\x0ablock.item\
 = /^( *)(bull) \
[^\x5cn]*(?:\x5cn(?!\x5c1\
bull )[^\x5cn]*)*/;\
\x0ablock.item = ed\
it(block.item, '\
gm')\x0a  .replace(\
/bull/g, block.b\
ullet)\x0a  .getReg\
ex();\x0a\x0ablock.lis\
t = edit(block.l\
ist)\x0a  .replace(\
/bull/g, block.b\
ullet)\x0a  .replac\
e('hr', '\x5c\x5cn+(?=\
\x5c\x5c1?(?:(?:- *){3\
,}|(?:_ *){3,}|(\
?:\x5c\x5c* *){3,})(?:\
\x5c\x5cn+|$))')\x0a  .re\
place('def', '\x5c\x5c\
n+(?=' + block.d\
ef.source + ')')\
\x0a  .getRegex();\x0a\
\x0ablock._tag = 'a\
ddress|article|a\
side|base|basefo\
nt|blockquote|bo\
dy|caption'\x0a  + \
'|center|col|col\
group|dd|details\
|dialog|dir|div|\
dl|dt|fieldset|f\
igcaption'\x0a  + '\
|figure|footer|f\
orm|frame|frames\
et|h[1-6]|head|h\
eader|hr|html|if\
rame'\x0a  + '|lege\
nd|li|link|main|\
menu|menuitem|me\
ta|nav|noframes|\
ol|optgroup|opti\
on'\x0a  + '|p|para\
m|section|source\
|summary|table|t\
body|td|tfoot|th\
|thead|title|tr'\
\x0a  + '|track|ul'\
;\x0ablock._comment\
 = /<!--(?!-?>)[\
\x5cs\x5cS]*?-->/;\x0ablo\
ck.html = edit(b\
lock.html, 'i')\x0a\
  .replace('comm\
ent', block._com\
ment)\x0a  .replace\
('tag', block._t\
ag)\x0a  .replace('\
attribute', / +[\
a-zA-Z:_][\x5cw.:-]\
*(?: *= *\x22[^\x22\x5cn]\
*\x22| *= *'[^'\x5cn]*\
'| *= *[^\x5cs\x22'=<>\
`]+)?/)\x0a  .getRe\
gex();\x0a\x0ablock.pa\
ragraph = edit(b\
lock.paragraph)\x0a\
  .replace('hr',\
 block.hr)\x0a  .re\
place('heading',\
 block.heading)\x0a\
  .replace('lhea\
ding', block.lhe\
ading)\x0a  .replac\
e('tag', block._\
tag) // pars can\
 be interrupted \
by type (6) html\
 blocks\x0a  .getRe\
gex();\x0a\x0ablock.bl\
ockquote = edit(\
block.blockquote\
)\x0a  .replace('pa\
ragraph', block.\
paragraph)\x0a  .ge\
tRegex();\x0a\x0a/**\x0a \
* Normal Block G\
rammar\x0a */\x0a\x0abloc\
k.normal = merge\
({}, block);\x0a\x0a/*\
*\x0a * GFM Block G\
rammar\x0a */\x0a\x0abloc\
k.gfm = merge({}\
, block.normal, \
{\x0a  fences: /^ *\
(`{3,}|~{3,})[ \x5c\
.]*(\x5cS+)? *\x5cn([\x5c\
s\x5cS]*?)\x5cn? *\x5c1 *\
(?:\x5cn+|$)/,\x0a  pa\
ragraph: /^/,\x0a  \
heading: /^ *(#{\
1,6}) +([^\x5cn]+?)\
 *#* *(?:\x5cn+|$)/\
\x0a});\x0a\x0ablock.gfm.\
paragraph = edit\
(block.paragraph\
)\x0a  .replace('(?\
!', '(?!'\x0a    + \
block.gfm.fences\
.source.replace(\
'\x5c\x5c1', '\x5c\x5c2') + \
'|'\x0a    + block.\
list.source.repl\
ace('\x5c\x5c1', '\x5c\x5c3'\
) + '|')\x0a  .getR\
egex();\x0a\x0a/**\x0a * \
GFM + Tables Blo\
ck Grammar\x0a */\x0a\x0a\
block.tables = m\
erge({}, block.g\
fm, {\x0a  nptable:\
 /^ *([^|\x5cn ].*\x5c\
|.*)\x5cn *([-:]+ *\
\x5c|[-| :]*)(?:\x5cn(\
(?:.*[^>\x5cn ].*(?\
:\x5cn|$))*)\x5cn*|$)/\
,\x0a  table: /^ *\x5c\
|(.+)\x5cn *\x5c|?( *[\
-:]+[-| :]*)(?:\x5c\
n((?: *[^>\x5cn ].*\
(?:\x5cn|$))*)\x5cn*|$\
)/\x0a});\x0a\x0a/**\x0a * P\
edantic grammar\x0a\
 */\x0a\x0ablock.pedan\
tic = merge({}, \
block.normal, {\x0a\
  html: edit(\x0a  \
  '^ *(?:comment\
 *(?:\x5c\x5cn|\x5c\x5cs*$)'\
\x0a    + '|<(tag)[\
\x5c\x5cs\x5c\x5cS]+?</\x5c\x5c1> \
*(?:\x5c\x5cn{2,}|\x5c\x5cs*\
$)' // closed ta\
g\x0a    + '|<tag(?\
:\x22[^\x22]*\x22|\x5c'[^\x5c']\
*\x5c'|\x5c\x5cs[^\x5c'\x22/>\x5c\x5c\
s]*)*?/?> *(?:\x5c\x5c\
n{2,}|\x5c\x5cs*$))')\x0a\
    .replace('co\
mment', block._c\
omment)\x0a    .rep\
lace(/tag/g, '(?\
!(?:'\x0a      + 'a\
|em|strong|small\
|s|cite|q|dfn|ab\
br|data|time|cod\
e|var|samp|kbd|s\
ub'\x0a      + '|su\
p|i|b|u|mark|rub\
y|rt|rp|bdi|bdo|\
span|br|wbr|ins|\
del|img)'\x0a      \
+ '\x5c\x5cb)\x5c\x5cw+(?!:|\
[^\x5c\x5cw\x5c\x5cs@]*@)\x5c\x5cb\
')\x0a    .getRegex\
(),\x0a  def: /^ *\x5c\
[([^\x5c]]+)\x5c]: *<?\
([^\x5cs>]+)>?(?: +\
([\x22(][^\x5cn]+[\x22)])\
)? *(?:\x5cn+|$)/\x0a}\
);\x0a\x0a/**\x0a * Block\
 Lexer\x0a */\x0a\x0afunc\
tion Lexer(optio\
ns) {\x0a  this.tok\
ens = [];\x0a  this\
.tokens.links = \
{};\x0a  this.optio\
ns = options || \
marked.defaults;\
\x0a  this.rules = \
block.normal;\x0a\x0a \
 if (this.option\
s.pedantic) {\x0a  \
  this.rules = b\
lock.pedantic;\x0a \
 } else if (this\
.options.gfm) {\x0a\
    if (this.opt\
ions.tables) {\x0a \
     this.rules \
= block.tables;\x0a\
    } else {\x0a   \
   this.rules = \
block.gfm;\x0a    }\
\x0a  }\x0a}\x0a\x0a/**\x0a * E\
xpose Block Rule\
s\x0a */\x0a\x0aLexer.rul\
es = block;\x0a\x0a/**\
\x0a * Static Lex M\
ethod\x0a */\x0a\x0aLexer\
.lex = function(\
src, options) {\x0a\
  var lexer = ne\
w Lexer(options)\
;\x0a  return lexer\
.lex(src);\x0a};\x0a\x0a/\
**\x0a * Preprocess\
ing\x0a */\x0a\x0aLexer.p\
rototype.lex = f\
unction(src) {\x0a \
 src = src\x0a    .\
replace(/\x5cr\x5cn|\x5cr\
/g, '\x5cn')\x0a    .r\
eplace(/\x5ct/g, ' \
   ')\x0a    .repla\
ce(/\x5cu00a0/g, ' \
')\x0a    .replace(\
/\x5cu2424/g, '\x5cn')\
;\x0a\x0a  return this\
.token(src, true\
);\x0a};\x0a\x0a/**\x0a * Le\
xing\x0a */\x0a\x0aLexer.\
prototype.token \
= function(src, \
top) {\x0a  src = s\
rc.replace(/^ +$\
/gm, '');\x0a  var \
next,\x0a      loos\
e,\x0a      cap,\x0a  \
    bull,\x0a      \
b,\x0a      item,\x0a \
     space,\x0a    \
  i,\x0a      tag,\x0a\
      l,\x0a      i\
sordered,\x0a      \
istask,\x0a      is\
checked;\x0a\x0a  whil\
e (src) {\x0a    //\
 newline\x0a    if \
(cap = this.rule\
s.newline.exec(s\
rc)) {\x0a      src\
 = src.substring\
(cap[0].length);\
\x0a      if (cap[0\
].length > 1) {\x0a\
        this.tok\
ens.push({\x0a     \
     type: 'spac\
e'\x0a        });\x0a \
     }\x0a    }\x0a\x0a  \
  // code\x0a    if\
 (cap = this.rul\
es.code.exec(src\
)) {\x0a      src =\
 src.substring(c\
ap[0].length);\x0a \
     cap = cap[0\
].replace(/^ {4}\
/gm, '');\x0a      \
this.tokens.push\
({\x0a        type:\
 'code',\x0a       \
 text: !this.opt\
ions.pedantic\x0a  \
        ? cap.re\
place(/\x5cn+$/, ''\
)\x0a          : ca\
p\x0a      });\x0a    \
  continue;\x0a    \
}\x0a\x0a    // fences\
 (gfm)\x0a    if (c\
ap = this.rules.\
fences.exec(src)\
) {\x0a      src = \
src.substring(ca\
p[0].length);\x0a  \
    this.tokens.\
push({\x0a        t\
ype: 'code',\x0a   \
     lang: cap[2\
],\x0a        text:\
 cap[3] || ''\x0a  \
    });\x0a      co\
ntinue;\x0a    }\x0a\x0a \
   // heading\x0a  \
  if (cap = this\
.rules.heading.e\
xec(src)) {\x0a    \
  src = src.subs\
tring(cap[0].len\
gth);\x0a      this\
.tokens.push({\x0a \
       type: 'he\
ading',\x0a        \
depth: cap[1].le\
ngth,\x0a        te\
xt: cap[2]\x0a     \
 });\x0a      conti\
nue;\x0a    }\x0a\x0a    \
// table no lead\
ing pipe (gfm)\x0a \
   if (top && (c\
ap = this.rules.\
nptable.exec(src\
))) {\x0a      item\
 = {\x0a        typ\
e: 'table',\x0a    \
    header: spli\
tCells(cap[1].re\
place(/^ *| *\x5c| \
*$/g, '')),\x0a    \
    align: cap[2\
].replace(/^ *|\x5c\
| *$/g, '').spli\
t(/ *\x5c| */),\x0a   \
     cells: cap[\
3] ? cap[3].repl\
ace(/\x5cn$/, '').s\
plit('\x5cn') : []\x0a\
      };\x0a\x0a      \
if (item.header.\
length === item.\
align.length) {\x0a\
        src = sr\
c.substring(cap[\
0].length);\x0a\x0a   \
     for (i = 0;\
 i < item.align.\
length; i++) {\x0a \
         if (/^ \
*-+: *$/.test(it\
em.align[i])) {\x0a\
            item\
.align[i] = 'rig\
ht';\x0a          }\
 else if (/^ *:-\
+: *$/.test(item\
.align[i])) {\x0a  \
          item.a\
lign[i] = 'cente\
r';\x0a          } \
else if (/^ *:-+\
 *$/.test(item.a\
lign[i])) {\x0a    \
        item.ali\
gn[i] = 'left';\x0a\
          } else\
 {\x0a            i\
tem.align[i] = n\
ull;\x0a          }\
\x0a        }\x0a\x0a    \
    for (i = 0; \
i < item.cells.l\
ength; i++) {\x0a  \
        item.cel\
ls[i] = splitCel\
ls(item.cells[i]\
, item.header.le\
ngth);\x0a        }\
\x0a\x0a        this.t\
okens.push(item)\
;\x0a\x0a        conti\
nue;\x0a      }\x0a   \
 }\x0a\x0a    // hr\x0a  \
  if (cap = this\
.rules.hr.exec(s\
rc)) {\x0a      src\
 = src.substring\
(cap[0].length);\
\x0a      this.toke\
ns.push({\x0a      \
  type: 'hr'\x0a   \
   });\x0a      con\
tinue;\x0a    }\x0a\x0a  \
  // blockquote\x0a\
    if (cap = th\
is.rules.blockqu\
ote.exec(src)) {\
\x0a      src = src\
.substring(cap[0\
].length);\x0a\x0a    \
  this.tokens.pu\
sh({\x0a        typ\
e: 'blockquote_s\
tart'\x0a      });\x0a\
\x0a      cap = cap\
[0].replace(/^ *\
> ?/gm, '');\x0a\x0a  \
    // Pass `top\
` to keep the cu\
rrent\x0a      // \x22\
toplevel\x22 state.\
 This is exactly\
\x0a      // how ma\
rkdown.pl works.\
\x0a      this.toke\
n(cap, top);\x0a\x0a  \
    this.tokens.\
push({\x0a        t\
ype: 'blockquote\
_end'\x0a      });\x0a\
\x0a      continue;\
\x0a    }\x0a\x0a    // l\
ist\x0a    if (cap \
= this.rules.lis\
t.exec(src)) {\x0a \
     src = src.s\
ubstring(cap[0].\
length);\x0a      b\
ull = cap[2];\x0a  \
    isordered = \
bull.length > 1;\
\x0a\x0a      this.tok\
ens.push({\x0a     \
   type: 'list_s\
tart',\x0a        o\
rdered: isordere\
d,\x0a        start\
: isordered ? +b\
ull : ''\x0a      }\
);\x0a\x0a      // Get\
 each top-level \
item.\x0a      cap \
= cap[0].match(t\
his.rules.item);\
\x0a\x0a      next = f\
alse;\x0a      l = \
cap.length;\x0a    \
  i = 0;\x0a\x0a      \
for (; i < l; i+\
+) {\x0a        ite\
m = cap[i];\x0a\x0a   \
     // Remove t\
he list item's b\
ullet\x0a        //\
 so it is seen a\
s the next token\
.\x0a        space \
= item.length;\x0a \
       item = it\
em.replace(/^ *(\
[*+-]|\x5cd+\x5c.) +/,\
 '');\x0a\x0a        /\
/ Outdent whatev\
er the\x0a        /\
/ list item cont\
ains. Hacky.\x0a   \
     if (~item.i\
ndexOf('\x5cn ')) {\
\x0a          space\
 -= item.length;\
\x0a          item \
= !this.options.\
pedantic\x0a       \
     ? item.repl\
ace(new RegExp('\
^ {1,' + space +\
 '}', 'gm'), '')\
\x0a            : i\
tem.replace(/^ {\
1,4}/gm, '');\x0a  \
      }\x0a\x0a       \
 // Determine wh\
ether the next l\
ist item belongs\
 here.\x0a        /\
/ Backpedal if i\
t does not belon\
g in this list.\x0a\
        if (this\
.options.smartLi\
sts && i !== l -\
 1) {\x0a          \
b = block.bullet\
.exec(cap[i + 1]\
)[0];\x0a          \
if (bull !== b &\
& !(bull.length \
> 1 && b.length \
> 1)) {\x0a        \
    src = cap.sl\
ice(i + 1).join(\
'\x5cn') + src;\x0a   \
         i = l -\
 1;\x0a          }\x0a\
        }\x0a\x0a     \
   // Determine \
whether item is \
loose or not.\x0a  \
      // Use: /(\
^|\x5cn)(?! )[^\x5cn]+\
\x5cn\x5cn(?!\x5cs*$)/\x0a  \
      // for dis\
count behavior.\x0a\
        loose = \
next || /\x5cn\x5cn(?!\
\x5cs*$)/.test(item\
);\x0a        if (i\
 !== l - 1) {\x0a  \
        next = i\
tem.charAt(item.\
length - 1) === \
'\x5cn';\x0a          \
if (!loose) loos\
e = next;\x0a      \
  }\x0a\x0a        // \
Check for task l\
ist items\x0a      \
  istask = /^\x5c[[\
 xX]\x5c] /.test(it\
em);\x0a        isc\
hecked = undefin\
ed;\x0a        if (\
istask) {\x0a      \
    ischecked = \
item[1] !== ' ';\
\x0a          item \
= item.replace(/\
^\x5c[[ xX]\x5c] +/, '\
');\x0a        }\x0a\x0a \
       this.toke\
ns.push({\x0a      \
    type: loose\x0a\
            ? 'l\
oose_item_start'\
\x0a            : '\
list_item_start'\
,\x0a          task\
: istask,\x0a      \
    checked: isc\
hecked\x0a        }\
);\x0a\x0a        // R\
ecurse.\x0a        \
this.token(item,\
 false);\x0a\x0a      \
  this.tokens.pu\
sh({\x0a          t\
ype: 'list_item_\
end'\x0a        });\
\x0a      }\x0a\x0a      \
this.tokens.push\
({\x0a        type:\
 'list_end'\x0a    \
  });\x0a\x0a      con\
tinue;\x0a    }\x0a\x0a  \
  // html\x0a    if\
 (cap = this.rul\
es.html.exec(src\
)) {\x0a      src =\
 src.substring(c\
ap[0].length);\x0a \
     this.tokens\
.push({\x0a        \
type: this.optio\
ns.sanitize\x0a    \
      ? 'paragra\
ph'\x0a          : \
'html',\x0a        \
pre: !this.optio\
ns.sanitizer\x0a   \
       && (cap[1\
] === 'pre' || c\
ap[1] === 'scrip\
t' || cap[1] ===\
 'style'),\x0a     \
   text: cap[0]\x0a\
      });\x0a      \
continue;\x0a    }\x0a\
\x0a    // def\x0a    \
if (top && (cap \
= this.rules.def\
.exec(src))) {\x0a \
     src = src.s\
ubstring(cap[0].\
length);\x0a      i\
f (cap[3]) cap[3\
] = cap[3].subst\
ring(1, cap[3].l\
ength - 1);\x0a    \
  tag = cap[1].t\
oLowerCase().rep\
lace(/\x5cs+/g, ' '\
);\x0a      if (!th\
is.tokens.links[\
tag]) {\x0a        \
this.tokens.link\
s[tag] = {\x0a     \
     href: cap[2\
],\x0a          tit\
le: cap[3]\x0a     \
   };\x0a      }\x0a  \
    continue;\x0a  \
  }\x0a\x0a    // tabl\
e (gfm)\x0a    if (\
top && (cap = th\
is.rules.table.e\
xec(src))) {\x0a   \
   item = {\x0a    \
    type: 'table\
',\x0a        heade\
r: splitCells(ca\
p[1].replace(/^ \
*| *\x5c| *$/g, '')\
),\x0a        align\
: cap[2].replace\
(/^ *|\x5c| *$/g, '\
').split(/ *\x5c| *\
/),\x0a        cell\
s: cap[3] ? cap[\
3].replace(/(?: \
*\x5c| *)?\x5cn$/, '')\
.split('\x5cn') : [\
]\x0a      };\x0a\x0a    \
  if (item.heade\
r.length === ite\
m.align.length) \
{\x0a        src = \
src.substring(ca\
p[0].length);\x0a\x0a \
       for (i = \
0; i < item.alig\
n.length; i++) {\
\x0a          if (/\
^ *-+: *$/.test(\
item.align[i])) \
{\x0a            it\
em.align[i] = 'r\
ight';\x0a         \
 } else if (/^ *\
:-+: *$/.test(it\
em.align[i])) {\x0a\
            item\
.align[i] = 'cen\
ter';\x0a          \
} else if (/^ *:\
-+ *$/.test(item\
.align[i])) {\x0a  \
          item.a\
lign[i] = 'left'\
;\x0a          } el\
se {\x0a           \
 item.align[i] =\
 null;\x0a         \
 }\x0a        }\x0a\x0a  \
      for (i = 0\
; i < item.cells\
.length; i++) {\x0a\
          item.c\
ells[i] = splitC\
ells(\x0a          \
  item.cells[i].\
replace(/^ *\x5c| *\
| *\x5c| *$/g, ''),\
\x0a            ite\
m.header.length)\
;\x0a        }\x0a\x0a   \
     this.tokens\
.push(item);\x0a\x0a  \
      continue;\x0a\
      }\x0a    }\x0a\x0a \
   // lheading\x0a \
   if (cap = thi\
s.rules.lheading\
.exec(src)) {\x0a  \
    src = src.su\
bstring(cap[0].l\
ength);\x0a      th\
is.tokens.push({\
\x0a        type: '\
heading',\x0a      \
  depth: cap[2] \
=== '=' ? 1 : 2,\
\x0a        text: c\
ap[1]\x0a      });\x0a\
      continue;\x0a\
    }\x0a\x0a    // to\
p-level paragrap\
h\x0a    if (top &&\
 (cap = this.rul\
es.paragraph.exe\
c(src))) {\x0a     \
 src = src.subst\
ring(cap[0].leng\
th);\x0a      this.\
tokens.push({\x0a  \
      type: 'par\
agraph',\x0a       \
 text: cap[1].ch\
arAt(cap[1].leng\
th - 1) === '\x5cn'\
\x0a          ? cap\
[1].slice(0, -1)\
\x0a          : cap\
[1]\x0a      });\x0a  \
    continue;\x0a  \
  }\x0a\x0a    // text\
\x0a    if (cap = t\
his.rules.text.e\
xec(src)) {\x0a    \
  // Top-level s\
hould never reac\
h here.\x0a      sr\
c = src.substrin\
g(cap[0].length)\
;\x0a      this.tok\
ens.push({\x0a     \
   type: 'text',\
\x0a        text: c\
ap[0]\x0a      });\x0a\
      continue;\x0a\
    }\x0a\x0a    if (s\
rc) {\x0a      thro\
w new Error('Inf\
inite loop on by\
te: ' + src.char\
CodeAt(0));\x0a    \
}\x0a  }\x0a\x0a  return \
this.tokens;\x0a};\x0a\
\x0a/**\x0a * Inline-L\
evel Grammar\x0a */\
\x0a\x0avar inline = {\
\x0a  escape: /^\x5c\x5c(\
[!\x22#$%&'()*+,\x5c-.\
/:;<=>?@\x5c[\x5c]\x5c\x5c^_\
`{|}~])/,\x0a  auto\
link: /^<(scheme\
:[^\x5cs\x5cx00-\x5cx1f<>\
]*|email)>/,\x0a  u\
rl: noop,\x0a  tag:\
 '^comment'\x0a    \
+ '|^</[a-zA-Z][\
\x5c\x5cw:-]*\x5c\x5cs*>' //\
 self-closing ta\
g\x0a    + '|^<[a-z\
A-Z][\x5c\x5cw-]*(?:at\
tribute)*?\x5c\x5cs*/?\
>' // open tag\x0a \
   + '|^<\x5c\x5c?[\x5c\x5cs\
\x5c\x5cS]*?\x5c\x5c?>' // p\
rocessing instru\
ction, e.g. <?ph\
p ?>\x0a    + '|^<!\
[a-zA-Z]+\x5c\x5cs[\x5c\x5cs\
\x5c\x5cS]*?>' // decl\
aration, e.g. <!\
DOCTYPE html>\x0a  \
  + '|^<!\x5c\x5c[CDAT\
A\x5c\x5c[[\x5c\x5cs\x5c\x5cS]*?\x5c\x5c\
]\x5c\x5c]>', // CDATA\
 section\x0a  link:\
 /^!?\x5c[(label)\x5c]\
\x5c(href(?:\x5cs+(tit\
le))?\x5cs*\x5c)/,\x0a  r\
eflink: /^!?\x5c[(l\
abel)\x5c]\x5c[(?!\x5cs*\x5c\
])((?:\x5c\x5c[\x5c[\x5c]]?|\
[^\x5c[\x5c]\x5c\x5c])+)\x5c]/,\
\x0a  nolink: /^!?\x5c\
[(?!\x5cs*\x5c])((?:\x5c[\
[^\x5c[\x5c]]*\x5c]|\x5c\x5c[\x5c[\
\x5c]]|[^\x5c[\x5c]])*)\x5c]\
(?:\x5c[\x5c])?/,\x0a  st\
rong: /^__([^\x5cs]\
[\x5cs\x5cS]*?[^\x5cs])__\
(?!_)|^\x5c*\x5c*([^\x5cs\
][\x5cs\x5cS]*?[^\x5cs])\x5c\
*\x5c*(?!\x5c*)|^__([^\
\x5cs])__(?!_)|^\x5c*\x5c\
*([^\x5cs])\x5c*\x5c*(?!\x5c\
*)/,\x0a  em: /^_([\
^\x5cs][\x5cs\x5cS]*?[^\x5cs\
_])_(?!_)|^_([^\x5c\
s_][\x5cs\x5cS]*?[^\x5cs]\
)_(?!_)|^\x5c*([^\x5cs\
][\x5cs\x5cS]*?[^\x5cs*])\
\x5c*(?!\x5c*)|^\x5c*([^\x5c\
s*][\x5cs\x5cS]*?[^\x5cs]\
)\x5c*(?!\x5c*)|^_([^\x5c\
s_])_(?!_)|^\x5c*([\
^\x5cs*])\x5c*(?!\x5c*)/,\
\x0a  code: /^(`+)\x5c\
s*([\x5cs\x5cS]*?[^`]?\
)\x5cs*\x5c1(?!`)/,\x0a  \
br: /^ {2,}\x5cn(?!\
\x5cs*$)/,\x0a  del: n\
oop,\x0a  text: /^[\
\x5cs\x5cS]+?(?=[\x5c\x5c<!\x5c\
[`*]|\x5cb_| {2,}\x5cn\
|$)/\x0a};\x0a\x0ainline.\
_escapes = /\x5c\x5c([\
!\x22#$%&'()*+,\x5c-./\
:;<=>?@\x5c[\x5c]\x5c\x5c^_`\
{|}~])/g;\x0a\x0ainlin\
e._scheme = /[a-\
zA-Z][a-zA-Z0-9+\
.-]{1,31}/;\x0ainli\
ne._email = /[a-\
zA-Z0-9.!#$%&'*+\
/=?^_`{|}~-]+(@)\
[a-zA-Z0-9](?:[a\
-zA-Z0-9-]{0,61}\
[a-zA-Z0-9])?(?:\
\x5c.[a-zA-Z0-9](?:\
[a-zA-Z0-9-]{0,6\
1}[a-zA-Z0-9])?)\
+(?![-_])/;\x0ainli\
ne.autolink = ed\
it(inline.autoli\
nk)\x0a  .replace('\
scheme', inline.\
_scheme)\x0a  .repl\
ace('email', inl\
ine._email)\x0a  .g\
etRegex();\x0a\x0ainli\
ne._attribute = \
/\x5cs+[a-zA-Z:_][\x5c\
w.:-]*(?:\x5cs*=\x5cs*\
\x22[^\x22]*\x22|\x5cs*=\x5cs*'\
[^']*'|\x5cs*=\x5cs*[^\
\x5cs\x22'=<>`]+)?/;\x0a\x0a\
inline.tag = edi\
t(inline.tag)\x0a  \
.replace('commen\
t', block._comme\
nt)\x0a  .replace('\
attribute', inli\
ne._attribute)\x0a \
 .getRegex();\x0a\x0ai\
nline._label = /\
(?:\x5c[[^\x5c[\x5c]]*\x5c]|\
\x5c\x5c[\x5c[\x5c]]?|`[^`]*\
`|[^\x5c[\x5c]\x5c\x5c])*?/;\
\x0ainline._href = \
/\x5cs*(<(?:\x5c\x5c[<>]?\
|[^\x5cs<>\x5c\x5c])*>|(?\
:\x5c\x5c[()]?|\x5c([^\x5cs\x5c\
x00-\x5cx1f()\x5c\x5c]*\x5c)\
|[^\x5cs\x5cx00-\x5cx1f()\
\x5c\x5c])*?)/;\x0ainline\
._title = /\x22(?:\x5c\
\x5c\x22?|[^\x22\x5c\x5c])*\x22|'(\
?:\x5c\x5c'?|[^'\x5c\x5c])*'\
|\x5c((?:\x5c\x5c\x5c)?|[^)\x5c\
\x5c])*\x5c)/;\x0a\x0ainline\
.link = edit(inl\
ine.link)\x0a  .rep\
lace('label', in\
line._label)\x0a  .\
replace('href', \
inline._href)\x0a  \
.replace('title'\
, inline._title)\
\x0a  .getRegex();\x0a\
\x0ainline.reflink \
= edit(inline.re\
flink)\x0a  .replac\
e('label', inlin\
e._label)\x0a  .get\
Regex();\x0a\x0a/**\x0a *\
 Normal Inline G\
rammar\x0a */\x0a\x0ainli\
ne.normal = merg\
e({}, inline);\x0a\x0a\
/**\x0a * Pedantic \
Inline Grammar\x0a \
*/\x0a\x0ainline.pedan\
tic = merge({}, \
inline.normal, {\
\x0a  strong: /^__(\
?=\x5cS)([\x5cs\x5cS]*?\x5cS\
)__(?!_)|^\x5c*\x5c*(?\
=\x5cS)([\x5cs\x5cS]*?\x5cS)\
\x5c*\x5c*(?!\x5c*)/,\x0a  e\
m: /^_(?=\x5cS)([\x5cs\
\x5cS]*?\x5cS)_(?!_)|^\
\x5c*(?=\x5cS)([\x5cs\x5cS]*\
?\x5cS)\x5c*(?!\x5c*)/,\x0a \
 link: edit(/^!?\
\x5c[(label)\x5c]\x5c((.*\
?)\x5c)/)\x0a    .repl\
ace('label', inl\
ine._label)\x0a    \
.getRegex(),\x0a  r\
eflink: edit(/^!\
?\x5c[(label)\x5c]\x5cs*\x5c\
[([^\x5c]]*)\x5c]/)\x0a  \
  .replace('labe\
l', inline._labe\
l)\x0a    .getRegex\
()\x0a});\x0a\x0a/**\x0a * G\
FM Inline Gramma\
r\x0a */\x0a\x0ainline.gf\
m = merge({}, in\
line.normal, {\x0a \
 escape: edit(in\
line.escape).rep\
lace('])', '~|])\
').getRegex(),\x0a \
 url: edit(/^((?\
:ftp|https?):\x5c/\x5c\
/|www\x5c.)(?:[a-zA\
-Z0-9\x5c-]+\x5c.?)+[^\
\x5cs<]*|^email/)\x0a \
   .replace('ema\
il', inline._ema\
il)\x0a    .getRege\
x(),\x0a  _backpeda\
l: /(?:[^?!.,:;*\
_~()&]+|\x5c([^)]*\x5c\
)|&(?![a-zA-Z0-9\
]+;$)|[?!.,:;*_~\
)]+(?!$))+/,\x0a  d\
el: /^~~(?=\x5cS)([\
\x5cs\x5cS]*?\x5cS)~~/,\x0a \
 text: edit(inli\
ne.text)\x0a    .re\
place(']|', '~]|\
')\x0a    .replace(\
'|', '|https?://\
|ftp://|www\x5c\x5c.|[\
a-zA-Z0-9.!#$%&\x5c\
'*+/=?^_`{\x5c\x5c|}~-\
]+@|')\x0a    .getR\
egex()\x0a});\x0a\x0a/**\x0a\
 * GFM + Line Br\
eaks Inline Gram\
mar\x0a */\x0a\x0ainline.\
breaks = merge({\
}, inline.gfm, {\
\x0a  br: edit(inli\
ne.br).replace('\
{2,}', '*').getR\
egex(),\x0a  text: \
edit(inline.gfm.\
text).replace('{\
2,}', '*').getRe\
gex()\x0a});\x0a\x0a/**\x0a \
* Inline Lexer &\
 Compiler\x0a */\x0a\x0af\
unction InlineLe\
xer(links, optio\
ns) {\x0a  this.opt\
ions = options |\
| marked.default\
s;\x0a  this.links \
= links;\x0a  this.\
rules = inline.n\
ormal;\x0a  this.re\
nderer = this.op\
tions.renderer |\
| new Renderer()\
;\x0a  this.rendere\
r.options = this\
.options;\x0a\x0a  if \
(!this.links) {\x0a\
    throw new Er\
ror('Tokens arra\
y requires a `li\
nks` property.')\
;\x0a  }\x0a\x0a  if (thi\
s.options.pedant\
ic) {\x0a    this.r\
ules = inline.pe\
dantic;\x0a  } else\
 if (this.option\
s.gfm) {\x0a    if \
(this.options.br\
eaks) {\x0a      th\
is.rules = inlin\
e.breaks;\x0a    } \
else {\x0a      thi\
s.rules = inline\
.gfm;\x0a    }\x0a  }\x0a\
}\x0a\x0a/**\x0a * Expose\
 Inline Rules\x0a *\
/\x0a\x0aInlineLexer.r\
ules = inline;\x0a\x0a\
/**\x0a * Static Le\
xing/Compiling M\
ethod\x0a */\x0a\x0aInlin\
eLexer.output = \
function(src, li\
nks, options) {\x0a\
  var inline = n\
ew InlineLexer(l\
inks, options);\x0a\
  return inline.\
output(src);\x0a};\x0a\
\x0a/**\x0a * Lexing/C\
ompiling\x0a */\x0a\x0aIn\
lineLexer.protot\
ype.output = fun\
ction(src) {\x0a  v\
ar out = '',\x0a   \
   link,\x0a      t\
ext,\x0a      href,\
\x0a      title,\x0a  \
    cap;\x0a\x0a  whil\
e (src) {\x0a    //\
 escape\x0a    if (\
cap = this.rules\
.escape.exec(src\
)) {\x0a      src =\
 src.substring(c\
ap[0].length);\x0a \
     out += cap[\
1];\x0a      contin\
ue;\x0a    }\x0a\x0a    /\
/ autolink\x0a    i\
f (cap = this.ru\
les.autolink.exe\
c(src)) {\x0a      \
src = src.substr\
ing(cap[0].lengt\
h);\x0a      if (ca\
p[2] === '@') {\x0a\
        text = e\
scape(this.mangl\
e(cap[1]));\x0a    \
    href = 'mail\
to:' + text;\x0a   \
   } else {\x0a    \
    text = escap\
e(cap[1]);\x0a     \
   href = text;\x0a\
      }\x0a      ou\
t += this.render\
er.link(href, nu\
ll, text);\x0a     \
 continue;\x0a    }\
\x0a\x0a    // url (gf\
m)\x0a    if (!this\
.inLink && (cap \
= this.rules.url\
.exec(src))) {\x0a \
     cap[0] = th\
is.rules._backpe\
dal.exec(cap[0])\
[0];\x0a      src =\
 src.substring(c\
ap[0].length);\x0a \
     if (cap[2] \
=== '@') {\x0a     \
   text = escape\
(cap[0]);\x0a      \
  href = 'mailto\
:' + text;\x0a     \
 } else {\x0a      \
  text = escape(\
cap[0]);\x0a       \
 if (cap[1] === \
'www.') {\x0a      \
    href = 'http\
://' + text;\x0a   \
     } else {\x0a  \
        href = t\
ext;\x0a        }\x0a \
     }\x0a      out\
 += this.rendere\
r.link(href, nul\
l, text);\x0a      \
continue;\x0a    }\x0a\
\x0a    // tag\x0a    \
if (cap = this.r\
ules.tag.exec(sr\
c)) {\x0a      if (\
!this.inLink && \
/^<a /i.test(cap\
[0])) {\x0a        \
this.inLink = tr\
ue;\x0a      } else\
 if (this.inLink\
 && /^<\x5c/a>/i.te\
st(cap[0])) {\x0a  \
      this.inLin\
k = false;\x0a     \
 }\x0a      src = s\
rc.substring(cap\
[0].length);\x0a   \
   out += this.o\
ptions.sanitize\x0a\
        ? this.o\
ptions.sanitizer\
\x0a          ? thi\
s.options.saniti\
zer(cap[0])\x0a    \
      : escape(c\
ap[0])\x0a        :\
 cap[0]\x0a      co\
ntinue;\x0a    }\x0a\x0a \
   // link\x0a    i\
f (cap = this.ru\
les.link.exec(sr\
c)) {\x0a      src \
= src.substring(\
cap[0].length);\x0a\
      this.inLin\
k = true;\x0a      \
href = cap[2];\x0a \
     if (this.op\
tions.pedantic) \
{\x0a        link =\
 /^([^'\x22]*[^\x5cs])\
\x5cs+(['\x22])(.*)\x5c2/\
.exec(href);\x0a\x0a  \
      if (link) \
{\x0a          href\
 = link[1];\x0a    \
      title = li\
nk[3];\x0a        }\
 else {\x0a        \
  title = '';\x0a  \
      }\x0a      } \
else {\x0a        t\
itle = cap[3] ? \
cap[3].slice(1, \
-1) : '';\x0a      \
}\x0a      href = h\
ref.trim().repla\
ce(/^<([\x5cs\x5cS]*)>\
$/, '$1');\x0a     \
 out += this.out\
putLink(cap, {\x0a \
       href: Inl\
ineLexer.escapes\
(href),\x0a        \
title: InlineLex\
er.escapes(title\
)\x0a      });\x0a    \
  this.inLink = \
false;\x0a      con\
tinue;\x0a    }\x0a\x0a  \
  // reflink, no\
link\x0a    if ((ca\
p = this.rules.r\
eflink.exec(src)\
)\x0a        || (ca\
p = this.rules.n\
olink.exec(src))\
) {\x0a      src = \
src.substring(ca\
p[0].length);\x0a  \
    link = (cap[\
2] || cap[1]).re\
place(/\x5cs+/g, ' \
');\x0a      link =\
 this.links[link\
.toLowerCase()];\
\x0a      if (!link\
 || !link.href) \
{\x0a        out +=\
 cap[0].charAt(0\
);\x0a        src =\
 cap[0].substrin\
g(1) + src;\x0a    \
    continue;\x0a  \
    }\x0a      this\
.inLink = true;\x0a\
      out += thi\
s.outputLink(cap\
, link);\x0a      t\
his.inLink = fal\
se;\x0a      contin\
ue;\x0a    }\x0a\x0a    /\
/ strong\x0a    if \
(cap = this.rule\
s.strong.exec(sr\
c)) {\x0a      src \
= src.substring(\
cap[0].length);\x0a\
      out += thi\
s.renderer.stron\
g(this.output(ca\
p[4] || cap[3] |\
| cap[2] || cap[\
1]));\x0a      cont\
inue;\x0a    }\x0a\x0a   \
 // em\x0a    if (c\
ap = this.rules.\
em.exec(src)) {\x0a\
      src = src.\
substring(cap[0]\
.length);\x0a      \
out += this.rend\
erer.em(this.out\
put(cap[6] || ca\
p[5] || cap[4] |\
| cap[3] || cap[\
2] || cap[1]));\x0a\
      continue;\x0a\
    }\x0a\x0a    // co\
de\x0a    if (cap =\
 this.rules.code\
.exec(src)) {\x0a  \
    src = src.su\
bstring(cap[0].l\
ength);\x0a      ou\
t += this.render\
er.codespan(esca\
pe(cap[2].trim()\
, true));\x0a      \
continue;\x0a    }\x0a\
\x0a    // br\x0a    i\
f (cap = this.ru\
les.br.exec(src)\
) {\x0a      src = \
src.substring(ca\
p[0].length);\x0a  \
    out += this.\
renderer.br();\x0a \
     continue;\x0a \
   }\x0a\x0a    // del\
 (gfm)\x0a    if (c\
ap = this.rules.\
del.exec(src)) {\
\x0a      src = src\
.substring(cap[0\
].length);\x0a     \
 out += this.ren\
derer.del(this.o\
utput(cap[1]));\x0a\
      continue;\x0a\
    }\x0a\x0a    // te\
xt\x0a    if (cap =\
 this.rules.text\
.exec(src)) {\x0a  \
    src = src.su\
bstring(cap[0].l\
ength);\x0a      ou\
t += this.render\
er.text(escape(t\
his.smartypants(\
cap[0])));\x0a     \
 continue;\x0a    }\
\x0a\x0a    if (src) {\
\x0a      throw new\
 Error('Infinite\
 loop on byte: '\
 + src.charCodeA\
t(0));\x0a    }\x0a  }\
\x0a\x0a  return out;\x0a\
};\x0a\x0aInlineLexer.\
escapes = functi\
on(text) {\x0a  ret\
urn text ? text.\
replace(InlineLe\
xer.rules._escap\
es, '$1') : text\
;\x0a}\x0a\x0a/**\x0a * Comp\
ile Link\x0a */\x0a\x0aIn\
lineLexer.protot\
ype.outputLink =\
 function(cap, l\
ink) {\x0a  var hre\
f = link.href,\x0a \
     title = lin\
k.title ? escape\
(link.title) : n\
ull;\x0a\x0a  return c\
ap[0].charAt(0) \
!== '!'\x0a    ? th\
is.renderer.link\
(href, title, th\
is.output(cap[1]\
))\x0a    : this.re\
nderer.image(hre\
f, title, escape\
(cap[1]));\x0a};\x0a\x0a/\
**\x0a * Smartypant\
s Transformation\
s\x0a */\x0a\x0aInlineLex\
er.prototype.sma\
rtypants = funct\
ion(text) {\x0a  if\
 (!this.options.\
smartypants) ret\
urn text;\x0a  retu\
rn text\x0a    // e\
m-dashes\x0a    .re\
place(/---/g, '\x5c\
u2014')\x0a    // e\
n-dashes\x0a    .re\
place(/--/g, '\x5cu\
2013')\x0a    // op\
ening singles\x0a  \
  .replace(/(^|[\
-\x5cu2014/(\x5c[{\x22\x5cs]\
)'/g, '$1\x5cu2018'\
)\x0a    // closing\
 singles & apost\
rophes\x0a    .repl\
ace(/'/g, '\x5cu201\
9')\x0a    // openi\
ng doubles\x0a    .\
replace(/(^|[-\x5cu\
2014/(\x5c[{\x5cu2018\x5c\
s])\x22/g, '$1\x5cu201\
c')\x0a    // closi\
ng doubles\x0a    .\
replace(/\x22/g, '\x5c\
u201d')\x0a    // e\
llipses\x0a    .rep\
lace(/\x5c.{3}/g, '\
\x5cu2026');\x0a};\x0a\x0a/*\
*\x0a * Mangle Link\
s\x0a */\x0a\x0aInlineLex\
er.prototype.man\
gle = function(t\
ext) {\x0a  if (!th\
is.options.mangl\
e) return text;\x0a\
  var out = '',\x0a\
      l = text.l\
ength,\x0a      i =\
 0,\x0a      ch;\x0a\x0a \
 for (; i < l; i\
++) {\x0a    ch = t\
ext.charCodeAt(i\
);\x0a    if (Math.\
random() > 0.5) \
{\x0a      ch = 'x'\
 + ch.toString(1\
6);\x0a    }\x0a    ou\
t += '&#' + ch +\
 ';';\x0a  }\x0a\x0a  ret\
urn out;\x0a};\x0a\x0a/**\
\x0a * Renderer\x0a */\
\x0a\x0afunction Rende\
rer(options) {\x0a \
 this.options = \
options || marke\
d.defaults;\x0a}\x0a\x0aR\
enderer.prototyp\
e.code = functio\
n(code, lang, es\
caped) {\x0a  if (t\
his.options.high\
light) {\x0a    var\
 out = this.opti\
ons.highlight(co\
de, lang);\x0a    i\
f (out != null &\
& out !== code) \
{\x0a      escaped \
= true;\x0a      co\
de = out;\x0a    }\x0a\
  }\x0a\x0a  if (!lang\
) {\x0a    return '\
<pre><code>'\x0a   \
   + (escaped ? \
code : escape(co\
de, true))\x0a     \
 + '</code></pre\
>';\x0a  }\x0a\x0a  retur\
n '<pre><code cl\
ass=\x22'\x0a    + thi\
s.options.langPr\
efix\x0a    + escap\
e(lang, true)\x0a  \
  + '\x22>'\x0a    + (\
escaped ? code :\
 escape(code, tr\
ue))\x0a    + '</co\
de></pre>\x5cn';\x0a};\
\x0a\x0aRenderer.proto\
type.blockquote \
= function(quote\
) {\x0a  return '<b\
lockquote>\x5cn' + \
quote + '</block\
quote>\x5cn';\x0a};\x0a\x0aR\
enderer.prototyp\
e.html = functio\
n(html) {\x0a  retu\
rn html;\x0a};\x0a\x0aRen\
derer.prototype.\
heading = functi\
on(text, level, \
raw) {\x0a  if (thi\
s.options.header\
Ids) {\x0a    retur\
n '<h'\x0a      + l\
evel\x0a      + ' i\
d=\x22'\x0a      + thi\
s.options.header\
Prefix\x0a      + r\
aw.toLowerCase()\
.replace(/[^\x5cw]+\
/g, '-')\x0a      +\
 '\x22>'\x0a      + te\
xt\x0a      + '</h'\
\x0a      + level\x0a \
     + '>\x5cn';\x0a  \
}\x0a  // ignore ID\
s\x0a  return '<h' \
+ level + '>' + \
text + '</h' + l\
evel + '>\x5cn';\x0a};\
\x0a\x0aRenderer.proto\
type.hr = functi\
on() {\x0a  return \
this.options.xht\
ml ? '<hr/>\x5cn' :\
 '<hr>\x5cn';\x0a};\x0a\x0aR\
enderer.prototyp\
e.list = functio\
n(body, ordered,\
 start) {\x0a  var \
type = ordered ?\
 'ol' : 'ul',\x0a  \
    startatt = (\
ordered && start\
 !== 1) ? (' sta\
rt=\x22' + start + \
'\x22') : '';\x0a  ret\
urn '<' + type +\
 startatt + '>\x5cn\
' + body + '</' \
+ type + '>\x5cn';\x0a\
};\x0a\x0aRenderer.pro\
totype.listitem \
= function(text)\
 {\x0a  return '<li\
>' + text + '</l\
i>\x5cn';\x0a};\x0a\x0aRende\
rer.prototype.ch\
eckbox = functio\
n(checked) {\x0a  r\
eturn '<input '\x0a\
    + (checked ?\
 'checked=\x22\x22 ' :\
 '')\x0a    + 'disa\
bled=\x22\x22 type=\x22ch\
eckbox\x22'\x0a    + (\
this.options.xht\
ml ? ' /' : '')\x0a\
    + '> ';\x0a}\x0a\x0aR\
enderer.prototyp\
e.paragraph = fu\
nction(text) {\x0a \
 return '<p>' + \
text + '</p>\x5cn';\
\x0a};\x0a\x0aRenderer.pr\
ototype.table = \
function(header,\
 body) {\x0a  if (b\
ody) body = '<tb\
ody>' + body + '\
</tbody>';\x0a\x0a  re\
turn '<table>\x5cn'\
\x0a    + '<thead>\x5c\
n'\x0a    + header\x0a\
    + '</thead>\x5c\
n'\x0a    + body\x0a  \
  + '</table>\x5cn'\
;\x0a};\x0a\x0aRenderer.p\
rototype.tablero\
w = function(con\
tent) {\x0a  return\
 '<tr>\x5cn' + cont\
ent + '</tr>\x5cn';\
\x0a};\x0a\x0aRenderer.pr\
ototype.tablecel\
l = function(con\
tent, flags) {\x0a \
 var type = flag\
s.header ? 'th' \
: 'td';\x0a  var ta\
g = flags.align\x0a\
    ? '<' + type\
 + ' align=\x22' + \
flags.align + '\x22\
>'\x0a    : '<' + t\
ype + '>';\x0a  ret\
urn tag + conten\
t + '</' + type \
+ '>\x5cn';\x0a};\x0a\x0a// \
span level rende\
rer\x0aRenderer.pro\
totype.strong = \
function(text) {\
\x0a  return '<stro\
ng>' + text + '<\
/strong>';\x0a};\x0a\x0aR\
enderer.prototyp\
e.em = function(\
text) {\x0a  return\
 '<em>' + text +\
 '</em>';\x0a};\x0a\x0aRe\
nderer.prototype\
.codespan = func\
tion(text) {\x0a  r\
eturn '<code>' +\
 text + '</code>\
';\x0a};\x0a\x0aRenderer.\
prototype.br = f\
unction() {\x0a  re\
turn this.option\
s.xhtml ? '<br/>\
' : '<br>';\x0a};\x0a\x0a\
Renderer.prototy\
pe.del = functio\
n(text) {\x0a  retu\
rn '<del>' + tex\
t + '</del>';\x0a};\
\x0a\x0aRenderer.proto\
type.link = func\
tion(href, title\
, text) {\x0a  if (\
this.options.san\
itize) {\x0a    try\
 {\x0a      var pro\
t = decodeURICom\
ponent(unescape(\
href))\x0a        .\
replace(/[^\x5cw:]/\
g, '')\x0a        .\
toLowerCase();\x0a \
   } catch (e) {\
\x0a      return te\
xt;\x0a    }\x0a    if\
 (prot.indexOf('\
javascript:') ==\
= 0 || prot.inde\
xOf('vbscript:')\
 === 0 || prot.i\
ndexOf('data:') \
=== 0) {\x0a      r\
eturn text;\x0a    \
}\x0a  }\x0a  if (this\
.options.baseUrl\
 && !originIndep\
endentUrl.test(h\
ref)) {\x0a    href\
 = resolveUrl(th\
is.options.baseU\
rl, href);\x0a  }\x0a \
 try {\x0a    href \
= encodeURI(href\
).replace(/%25/g\
, '%');\x0a  } catc\
h (e) {\x0a    retu\
rn text;\x0a  }\x0a  v\
ar out = '<a hre\
f=\x22' + escape(hr\
ef) + '\x22';\x0a  if \
(title) {\x0a    ou\
t += ' title=\x22' \
+ title + '\x22';\x0a \
 }\x0a  out += '>' \
+ text + '</a>';\
\x0a  return out;\x0a}\
;\x0a\x0aRenderer.prot\
otype.image = fu\
nction(href, tit\
le, text) {\x0a  if\
 (this.options.b\
aseUrl && !origi\
nIndependentUrl.\
test(href)) {\x0a  \
  href = resolve\
Url(this.options\
.baseUrl, href);\
\x0a  }\x0a  var out =\
 '<img src=\x22' + \
href + '\x22 alt=\x22'\
 + text + '\x22';\x0a \
 if (title) {\x0a  \
  out += ' title\
=\x22' + title + '\x22\
';\x0a  }\x0a  out += \
this.options.xht\
ml ? '/>' : '>';\
\x0a  return out;\x0a}\
;\x0a\x0aRenderer.prot\
otype.text = fun\
ction(text) {\x0a  \
return text;\x0a};\x0a\
\x0a/**\x0a * TextRend\
erer\x0a * returns \
only the textual\
 part of the tok\
en\x0a */\x0a\x0afunction\
 TextRenderer() \
{}\x0a\x0a// no need f\
or block level r\
enderers\x0a\x0aTextRe\
nderer.prototype\
.strong =\x0aTextRe\
nderer.prototype\
.em =\x0aTextRender\
er.prototype.cod\
espan =\x0aTextRend\
erer.prototype.d\
el =\x0aTextRendere\
r.prototype.text\
 = function (tex\
t) {\x0a  return te\
xt;\x0a}\x0a\x0aTextRende\
rer.prototype.li\
nk =\x0aTextRendere\
r.prototype.imag\
e = function(hre\
f, title, text) \
{\x0a  return '' + \
text;\x0a}\x0a\x0aTextRen\
derer.prototype.\
br = function() \
{\x0a  return '';\x0a}\
\x0a\x0a/**\x0a * Parsing\
 & Compiling\x0a */\
\x0a\x0afunction Parse\
r(options) {\x0a  t\
his.tokens = [];\
\x0a  this.token = \
null;\x0a  this.opt\
ions = options |\
| marked.default\
s;\x0a  this.option\
s.renderer = thi\
s.options.render\
er || new Render\
er();\x0a  this.ren\
derer = this.opt\
ions.renderer;\x0a \
 this.renderer.o\
ptions = this.op\
tions;\x0a}\x0a\x0a/**\x0a *\
 Static Parse Me\
thod\x0a */\x0a\x0aParser\
.parse = functio\
n(src, options) \
{\x0a  var parser =\
 new Parser(opti\
ons);\x0a  return p\
arser.parse(src)\
;\x0a};\x0a\x0a/**\x0a * Par\
se Loop\x0a */\x0a\x0aPar\
ser.prototype.pa\
rse = function(s\
rc) {\x0a  this.inl\
ine = new Inline\
Lexer(src.links,\
 this.options);\x0a\
  // use an Inli\
neLexer with a T\
extRenderer to e\
xtract pure text\
\x0a  this.inlineTe\
xt = new InlineL\
exer(\x0a    src.li\
nks,\x0a    merge({\
}, this.options,\
 {renderer: new \
TextRenderer()})\
\x0a  );\x0a  this.tok\
ens = src.revers\
e();\x0a\x0a  var out \
= '';\x0a  while (t\
his.next()) {\x0a  \
  out += this.to\
k();\x0a  }\x0a\x0a  retu\
rn out;\x0a};\x0a\x0a/**\x0a\
 * Next Token\x0a *\
/\x0a\x0aParser.protot\
ype.next = funct\
ion() {\x0a  return\
 this.token = th\
is.tokens.pop();\
\x0a};\x0a\x0a/**\x0a * Prev\
iew Next Token\x0a \
*/\x0a\x0aParser.proto\
type.peek = func\
tion() {\x0a  retur\
n this.tokens[th\
is.tokens.length\
 - 1] || 0;\x0a};\x0a\x0a\
/**\x0a * Parse Tex\
t Tokens\x0a */\x0a\x0aPa\
rser.prototype.p\
arseText = funct\
ion() {\x0a  var bo\
dy = this.token.\
text;\x0a\x0a  while (\
this.peek().type\
 === 'text') {\x0a \
   body += '\x5cn' \
+ this.next().te\
xt;\x0a  }\x0a\x0a  retur\
n this.inline.ou\
tput(body);\x0a};\x0a\x0a\
/**\x0a * Parse Cur\
rent Token\x0a */\x0a\x0a\
Parser.prototype\
.tok = function(\
) {\x0a  switch (th\
is.token.type) {\
\x0a    case 'space\
': {\x0a      retur\
n '';\x0a    }\x0a    \
case 'hr': {\x0a   \
   return this.r\
enderer.hr();\x0a  \
  }\x0a    case 'he\
ading': {\x0a      \
return this.rend\
erer.heading(\x0a  \
      this.inlin\
e.output(this.to\
ken.text),\x0a     \
   this.token.de\
pth,\x0a        une\
scape(this.inlin\
eText.output(thi\
s.token.text)));\
\x0a    }\x0a    case \
'code': {\x0a      \
return this.rend\
erer.code(this.t\
oken.text,\x0a     \
   this.token.la\
ng,\x0a        this\
.token.escaped);\
\x0a    }\x0a    case \
'table': {\x0a     \
 var header = ''\
,\x0a          body\
 = '',\x0a         \
 i,\x0a          ro\
w,\x0a          cel\
l,\x0a          j;\x0a\
\x0a      // header\
\x0a      cell = ''\
;\x0a      for (i =\
 0; i < this.tok\
en.header.length\
; i++) {\x0a       \
 cell += this.re\
nderer.tablecell\
(\x0a          this\
.inline.output(t\
his.token.header\
[i]),\x0a          \
{ header: true, \
align: this.toke\
n.align[i] }\x0a   \
     );\x0a      }\x0a\
      header += \
this.renderer.ta\
blerow(cell);\x0a\x0a \
     for (i = 0;\
 i < this.token.\
cells.length; i+\
+) {\x0a        row\
 = this.token.ce\
lls[i];\x0a\x0a       \
 cell = '';\x0a    \
    for (j = 0; \
j < row.length; \
j++) {\x0a         \
 cell += this.re\
nderer.tablecell\
(\x0a            th\
is.inline.output\
(row[j]),\x0a      \
      { header: \
false, align: th\
is.token.align[j\
] }\x0a          );\
\x0a        }\x0a\x0a    \
    body += this\
.renderer.tabler\
ow(cell);\x0a      \
}\x0a      return t\
his.renderer.tab\
le(header, body)\
;\x0a    }\x0a    case\
 'blockquote_sta\
rt': {\x0a      bod\
y = '';\x0a\x0a      w\
hile (this.next(\
).type !== 'bloc\
kquote_end') {\x0a \
       body += t\
his.tok();\x0a     \
 }\x0a\x0a      return\
 this.renderer.b\
lockquote(body);\
\x0a    }\x0a    case \
'list_start': {\x0a\
      body = '';\
\x0a      var order\
ed = this.token.\
ordered,\x0a       \
   start = this.\
token.start;\x0a\x0a  \
    while (this.\
next().type !== \
'list_end') {\x0a  \
      body += th\
is.tok();\x0a      \
}\x0a\x0a      return \
this.renderer.li\
st(body, ordered\
, start);\x0a    }\x0a\
    case 'list_i\
tem_start': {\x0a  \
    body = '';\x0a\x0a\
      if (this.t\
oken.task) {\x0a   \
     body += thi\
s.renderer.check\
box(this.token.c\
hecked);\x0a      }\
\x0a\x0a      while (t\
his.next().type \
!== 'list_item_e\
nd') {\x0a        b\
ody += this.toke\
n.type === 'text\
'\x0a          ? th\
is.parseText()\x0a \
         : this.\
tok();\x0a      }\x0a\x0a\
      return thi\
s.renderer.listi\
tem(body);\x0a    }\
\x0a    case 'loose\
_item_start': {\x0a\
      body = '';\
\x0a\x0a      while (t\
his.next().type \
!== 'list_item_e\
nd') {\x0a        b\
ody += this.tok(\
);\x0a      }\x0a\x0a    \
  return this.re\
nderer.listitem(\
body);\x0a    }\x0a   \
 case 'html': {\x0a\
      // TODO pa\
rse inline conte\
nt if parameter \
markdown=1\x0a     \
 return this.ren\
derer.html(this.\
token.text);\x0a   \
 }\x0a    case 'par\
agraph': {\x0a     \
 return this.ren\
derer.paragraph(\
this.inline.outp\
ut(this.token.te\
xt));\x0a    }\x0a    \
case 'text': {\x0a \
     return this\
.renderer.paragr\
aph(this.parseTe\
xt());\x0a    }\x0a  }\
\x0a};\x0a\x0a/**\x0a * Help\
ers\x0a */\x0a\x0afunctio\
n escape(html, e\
ncode) {\x0a  retur\
n html\x0a    .repl\
ace(!encode ? /&\
(?!#?\x5cw+;)/g : /\
&/g, '&amp;')\x0a  \
  .replace(/</g,\
 '&lt;')\x0a    .re\
place(/>/g, '&gt\
;')\x0a    .replace\
(/\x22/g, '&quot;')\
\x0a    .replace(/'\
/g, '&#39;');\x0a}\x0a\
\x0afunction unesca\
pe(html) {\x0a  // \
explicitly match\
 decimal, hex, a\
nd named HTML en\
tities\x0a  return \
html.replace(/&(\
#(?:\x5cd+)|(?:#x[0\
-9A-Fa-f]+)|(?:\x5c\
w+));?/ig, funct\
ion(_, n) {\x0a    \
n = n.toLowerCas\
e();\x0a    if (n =\
== 'colon') retu\
rn ':';\x0a    if (\
n.charAt(0) === \
'#') {\x0a      ret\
urn n.charAt(1) \
=== 'x'\x0a        \
? String.fromCha\
rCode(parseInt(n\
.substring(2), 1\
6))\x0a        : St\
ring.fromCharCod\
e(+n.substring(1\
));\x0a    }\x0a    re\
turn '';\x0a  });\x0a}\
\x0a\x0afunction edit(\
regex, opt) {\x0a  \
regex = regex.so\
urce || regex;\x0a \
 opt = opt || ''\
;\x0a  return {\x0a   \
 replace: functi\
on(name, val) {\x0a\
      val = val.\
source || val;\x0a \
     val = val.r\
eplace(/(^|[^\x5c[]\
)\x5c^/g, '$1');\x0a  \
    regex = rege\
x.replace(name, \
val);\x0a      retu\
rn this;\x0a    },\x0a\
    getRegex: fu\
nction() {\x0a     \
 return new RegE\
xp(regex, opt);\x0a\
    }\x0a  };\x0a}\x0a\x0afu\
nction resolveUr\
l(base, href) {\x0a\
  if (!baseUrls[\
' ' + base]) {\x0a \
   // we can ign\
ore everything i\
n base after the\
 last slash of i\
ts path componen\
t,\x0a    // but we\
 might need to a\
dd _that_\x0a    //\
 https://tools.i\
etf.org/html/rfc\
3986#section-3\x0a \
   if (/^[^:]+:\x5c\
/*[^/]*$/.test(b\
ase)) {\x0a      ba\
seUrls[' ' + bas\
e] = base + '/';\
\x0a    } else {\x0a  \
    baseUrls[' '\
 + base] = base.\
replace(/[^/]*$/\
, '');\x0a    }\x0a  }\
\x0a  base = baseUr\
ls[' ' + base];\x0a\
\x0a  if (href.slic\
e(0, 2) === '//'\
) {\x0a    return b\
ase.replace(/:[\x5c\
s\x5cS]*/, ':') + h\
ref;\x0a  } else if\
 (href.charAt(0)\
 === '/') {\x0a    \
return base.repl\
ace(/(:\x5c/*[^/]*)\
[\x5cs\x5cS]*/, '$1') \
+ href;\x0a  } else\
 {\x0a    return ba\
se + href;\x0a  }\x0a}\
\x0avar baseUrls = \
{};\x0avar originIn\
dependentUrl = /\
^$|^[a-z][a-z0-9\
+.-]*:|^[?#]/i;\x0a\
\x0afunction noop()\
 {}\x0anoop.exec = \
noop;\x0a\x0afunction \
merge(obj) {\x0a  v\
ar i = 1,\x0a      \
target,\x0a      ke\
y;\x0a\x0a  for (; i <\
 arguments.lengt\
h; i++) {\x0a    ta\
rget = arguments\
[i];\x0a    for (ke\
y in target) {\x0a \
     if (Object.\
prototype.hasOwn\
Property.call(ta\
rget, key)) {\x0a  \
      obj[key] =\
 target[key];\x0a  \
    }\x0a    }\x0a  }\x0a\
\x0a  return obj;\x0a}\
\x0a\x0afunction split\
Cells(tableRow, \
count) {\x0a  var c\
ells = tableRow.\
replace(/([^\x5c\x5c])\
\x5c|/g, '$1 |').sp\
lit(/ +\x5c| */),\x0a \
     i = 0;\x0a\x0a  i\
f (cells.length \
> count) {\x0a    c\
ells.splice(coun\
t);\x0a  } else {\x0a \
   while (cells.\
length < count) \
cells.push('');\x0a\
  }\x0a\x0a  for (; i \
< cells.length; \
i++) {\x0a    cells\
[i] = cells[i].r\
eplace(/\x5c\x5c\x5c|/g, \
'|');\x0a  }\x0a  retu\
rn cells;\x0a}\x0a\x0a/**\
\x0a * Marked\x0a */\x0a\x0a\
function marked(\
src, opt, callba\
ck) {\x0a  // throw\
 error in case o\
f non string inp\
ut\x0a  if (typeof \
src === 'undefin\
ed' || src === n\
ull) {\x0a    throw\
 new Error('mark\
ed(): input para\
meter is undefin\
ed or null');\x0a  \
}\x0a  if (typeof s\
rc !== 'string')\
 {\x0a    throw new\
 Error('marked()\
: input paramete\
r is of type '\x0a \
     + Object.pr\
ototype.toString\
.call(src) + ', \
string expected'\
);\x0a  }\x0a\x0a  if (ca\
llback || typeof\
 opt === 'functi\
on') {\x0a    if (!\
callback) {\x0a    \
  callback = opt\
;\x0a      opt = nu\
ll;\x0a    }\x0a\x0a    o\
pt = merge({}, m\
arked.defaults, \
opt || {});\x0a\x0a   \
 var highlight =\
 opt.highlight,\x0a\
        tokens,\x0a\
        pending,\
\x0a        i = 0;\x0a\
\x0a    try {\x0a     \
 tokens = Lexer.\
lex(src, opt)\x0a  \
  } catch (e) {\x0a\
      return cal\
lback(e);\x0a    }\x0a\
\x0a    pending = t\
okens.length;\x0a\x0a \
   var done = fu\
nction(err) {\x0a  \
    if (err) {\x0a \
       opt.highl\
ight = highlight\
;\x0a        return\
 callback(err);\x0a\
      }\x0a\x0a      v\
ar out;\x0a\x0a      t\
ry {\x0a        out\
 = Parser.parse(\
tokens, opt);\x0a  \
    } catch (e) \
{\x0a        err = \
e;\x0a      }\x0a\x0a    \
  opt.highlight \
= highlight;\x0a\x0a  \
    return err\x0a \
       ? callbac\
k(err)\x0a        :\
 callback(null, \
out);\x0a    };\x0a\x0a  \
  if (!highlight\
 || highlight.le\
ngth < 3) {\x0a    \
  return done();\
\x0a    }\x0a\x0a    dele\
te opt.highlight\
;\x0a\x0a    if (!pend\
ing) return done\
();\x0a\x0a    for (; \
i < tokens.lengt\
h; i++) {\x0a      \
(function(token)\
 {\x0a        if (t\
oken.type !== 'c\
ode') {\x0a        \
  return --pendi\
ng || done();\x0a  \
      }\x0a        \
return highlight\
(token.text, tok\
en.lang, functio\
n(err, code) {\x0a \
         if (err\
) return done(er\
r);\x0a          if\
 (code == null |\
| code === token\
.text) {\x0a       \
     return --pe\
nding || done();\
\x0a          }\x0a   \
       token.tex\
t = code;\x0a      \
    token.escape\
d = true;\x0a      \
    --pending ||\
 done();\x0a       \
 });\x0a      })(to\
kens[i]);\x0a    }\x0a\
\x0a    return;\x0a  }\
\x0a  try {\x0a    if \
(opt) opt = merg\
e({}, marked.def\
aults, opt);\x0a   \
 return Parser.p\
arse(Lexer.lex(s\
rc, opt), opt);\x0a\
  } catch (e) {\x0a\
    e.message +=\
 '\x5cnPlease repor\
t this to https:\
//github.com/mar\
kedjs/marked.';\x0a\
    if ((opt || \
marked.defaults)\
.silent) {\x0a     \
 return '<p>An e\
rror occurred:</\
p><pre>'\x0a       \
 + escape(e.mess\
age + '', true)\x0a\
        + '</pre\
>';\x0a    }\x0a    th\
row e;\x0a  }\x0a}\x0a\x0a/*\
*\x0a * Options\x0a */\
\x0a\x0amarked.options\
 =\x0amarked.setOpt\
ions = function(\
opt) {\x0a  merge(m\
arked.defaults, \
opt);\x0a  return m\
arked;\x0a};\x0a\x0amarke\
d.getDefaults = \
function () {\x0a  \
return {\x0a    bas\
eUrl: null,\x0a    \
breaks: false,\x0a \
   gfm: true,\x0a  \
  headerIds: tru\
e,\x0a    headerPre\
fix: '',\x0a    hig\
hlight: null,\x0a  \
  langPrefix: 'l\
anguage-',\x0a    m\
angle: true,\x0a   \
 pedantic: false\
,\x0a    renderer: \
new Renderer(),\x0a\
    sanitize: fa\
lse,\x0a    sanitiz\
er: null,\x0a    si\
lent: false,\x0a   \
 smartLists: fal\
se,\x0a    smartypa\
nts: false,\x0a    \
tables: true,\x0a  \
  xhtml: false\x0a \
 };\x0a}\x0a\x0amarked.de\
faults = marked.\
getDefaults();\x0a\x0a\
/**\x0a * Expose\x0a *\
/\x0a\x0amarked.Parser\
 = Parser;\x0amarke\
d.parser = Parse\
r.parse;\x0a\x0amarked\
.Renderer = Rend\
erer;\x0amarked.Tex\
tRenderer = Text\
Renderer;\x0a\x0amarke\
d.Lexer = Lexer;\
\x0amarked.lexer = \
Lexer.lex;\x0a\x0amark\
ed.InlineLexer =\
 InlineLexer;\x0ama\
rked.inlineLexer\
 = InlineLexer.o\
utput;\x0a\x0amarked.p\
arse = marked;\x0a\x0a\
if (typeof modul\
e !== 'undefined\
' && typeof expo\
rts === 'object'\
) {\x0a  module.exp\
orts = marked;\x0a}\
 else if (typeof\
 define === 'fun\
ction' && define\
.amd) {\x0a  define\
(function() { re\
turn marked; });\
\x0a} else {\x0a  root\
.marked = marked\
;\x0a}\x0a})(this || (\
typeof window !=\
= 'undefined' ? \
window : global)\
);\x0a\
"

qt_resource_name = b"\
\x00\x08\
\x08\xb6\x8e\xf9\
\x003\
\x00r\x00d\x00p\x00a\x00r\x00t\x00y\
\x00\x0a\
\x08\xce\x22\xb4\
\x00d\
\x00e\x00f\x00a\x00u\x00l\x00t\x00.\x00m\x00d\
\x00\x0a\
\x0c\xba\xf2|\
\x00i\
\x00n\x00d\x00e\x00x\x00.\x00h\x00t\x00m\x00l\
\x00\x0c\
\x08\xd0i\xc3\
\x00m\
\x00a\x00r\x00k\x00d\x00o\x00w\x00n\x00.\x00c\x00s\x00s\
\x00\x09\
\x09\x1b\x92\x13\
\x00m\
\x00a\x00r\x00k\x00e\x00d\x00.\x00j\x00s\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x04\
\x00\x00\x00\x16\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x000\x00\x00\x00\x00\x00\x01\x00\x00\x01\xe1\
\x00\x00\x00J\x00\x00\x00\x00\x00\x01\x00\x00\x04\xa1\
\x00\x00\x00h\x00\x00\x00\x00\x00\x01\x00\x00\x1c\x0a\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
