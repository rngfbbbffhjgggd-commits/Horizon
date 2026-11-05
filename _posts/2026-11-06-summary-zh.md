---
layout: default
title: "Horizon Summary: 2026-11-06 (ZH)"
date: 2026-11-06
lang: zh
---

> 从 690 条内容中筛选出 25 条重要资讯。

---

1. [克里姆林宫关联黑客利用 iOS 和安卓漏洞发动外交间谍攻击](#item-1) ⭐️ 8.0/10
2. [香港活动家黄之锋因「勾结外国势力」被判囚 10 年](#item-2) ⭐️ 8.0/10
3. [民主党在 2026 年中期选举翻转数十众议院席位，扩大多数优势](#item-3) ⭐️ 8.0/10
4. [英国央行加息 25 个基点至 4% 为 2023 年以来首次](#item-4) ⭐️ 8.0/10
5. [英伟达 H200 芯片在香港堆积 因中国暂缓进口审批](#item-5) ⭐️ 8.0/10
6. [丁薛祥出席第九届进博会开幕式并提出四大原则促贸易平衡](#item-6) ⭐️ 8.0/10
7. [前政治局委员马兴瑞因受贿被起诉](#item-7) ⭐️ 8.0/10
8. [央视：东风-61 洲际导弹已列装火箭军](#item-8) ⭐️ 8.0/10
9. [中国地方融资平台数量三年半减少逾九成](#item-9) ⭐️ 8.0/10
10. [美联社独家：特朗普政府战时与伊朗秘密谈判遣返伊朗人](#item-10) ⭐️ 7.5/10
11. [sshole：通过 crypt\(\) 特殊哈希值绕过 SSH（Secure Shell）认证](#item-11) ⭐️ 7.0/10
12. [美国政府警告工业制冷系统面临持续网络威胁](#item-12) ⭐️ 7.0/10
13. [韩国在美压力下拟扩大海军行动至霍尔木兹海峡附近](#item-13) ⭐️ 7.0/10
14. [炸弹威胁扰乱欧洲 15 国 25 余航班](#item-14) ⭐️ 7.0/10
15. [也门总统解职部长和军官试图扭转战局](#item-15) ⭐️ 7.0/10
16. [伊朗通过卡塔尔向美国提交核提案并附带七项前提条件](#item-16) ⭐️ 7.0/10
17. [美国众院共和党要求英伟达 CEO 就中方间谍指控作简报](#item-17) ⭐️ 7.0/10
18. [伊朗最高国家安全委员会秘书礼萨伊会见普京](#item-18) ⭐️ 7.0/10
19. [幸运咖加盟商向蜜雪集团创始人求援，门店大幅关闭](#item-19) ⭐️ 7.0/10
20. [大众中国转让国轩高科 5.3%股份予合肥国资](#item-20) ⭐️ 7.0/10
21. [美国初请失业金人数降至 57 年低位；第三季度生产率飙升](#item-21) ⭐️ 7.0/10
22. [普京将日本烟草在俄资产置于临时管理](#item-22) ⭐️ 7.0/10
23. [伊朗在霍尔木兹海峡袭击油轮 回应美国中期选举](#item-23) ⭐️ 7.0/10
24. [梅洛尼警告欧洲在乌克兰和谈中面临边缘化风险](#item-24) ⭐️ 7.0/10
25. [无人机袭击俄罗斯梁赞炼油厂 导致主力装置停运](#item-25) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [克里姆林宫关联黑客利用 iOS 和安卓漏洞发动外交间谍攻击](https://arstechnica.com/security/2026/11/hackers-exploited-ios-and-android-flaws-to-infect-phones/) ⭐️ 8.0/10

安全研究人员披露，一个疑似由克里姆林宫（俄罗斯总统府）赞助的黑客组织利用 iOS 和安卓系统中已修补的漏洞，发动“水坑攻击”（watering hole attack）瞄准外交人员。攻击者入侵了多个网站——包括一个庆祝美国独立日的网站和一家靠近英国敏感政府机构的豪华酒店官网——通过 JavaScript 注入、代理域名和被劫持的乌克兰网络分析服务向访问者设备植入恶意软件。该行动被归因于俄罗斯对外情报局（SVR），利用已知漏洞利用（n-day exploits）攻击未打补丁的手机，而非零日漏洞（zero-day）。 此次行动表明，国家支持的攻击者能将已知漏洞大规模武器化针对高价值目标，无需昂贵的零日漏洞即可利用海量未打补丁设备。攻击目标锁定英国敏感政府机构附近的外交人员及美国独立日相关网站，显示这是一场具有潜在地缘政治后果的战略情报收集行动。全球数十亿 iOS 和安卓用户若延迟安装安全更新仍面临风险，因为被利用的漏洞在攻击开始前已有补丁可用。 攻击者利用被入侵的乌克兰网络分析服务向合法网站注入恶意 JavaScript，通过代理域名将访问者重定向至利用链，攻击 CVE（通用漏洞披露编号）-2024-23222（iOS 漏洞）和 CVE-2024-31320（安卓漏洞）——两者均在 2024 年初已修补。研究人员指出，该行动基础设施与先前 SVR（俄罗斯对外情报局）关联活动重叠，且瞄准英国政府通信总部（GCHQ）附近的酒店暗示了物理邻近情报目标。目前无证据显示漏洞利用对完全更新的设备生效，再次强调及时打补丁的重要性。

rss · Ars Technica · 11月5日 06:26

**背景**: “水坑攻击”——攻击者入侵特定目标群体常访问的网站——自 2012 年“Elderwood”行动针对国防承包商以来，已成为国家支持间谍活动的常用手段。俄罗斯对外情报局（SVR，前身为克格勃第一总局）有记录在案的复杂网络行动历史，包括 2020 年被归因于 APT29（高级持续性威胁组织 29 号，Cozy Bear）的 SolarWinds 供应链攻击。被利用的漏洞 CVE（通用漏洞披露编号）-2024-23222（WebKit 引擎）和 CVE-2024-31320（安卓框架）均允许通过恶意网页内容远程执行代码，分别于 2024 年 1 月和 2 月修补。JavaScript 注入仍是主要浏览器威胁载体，当网站未对输入进行清洗时可导致会话劫持和数据窃取。使用代理域名和被入侵的第三方服务（如乌克兰分析提供商）反映了通过供应链和基础设施劫持规避溯源的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Watering_hole_attack">Watering hole attack - Wikipedia</a></li>
<li><a href="https://www.feroot.com/education-center/what-is-a-javascript-injection-attack/">What is a JavaScript Injection Attack? - Feroot</a></li>
<li><a href="https://encyclopedia.pub/entry/28279">Domain Fronting | Encyclopedia MDPI</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#mobile security`, `#state-sponsored hacking`, `#iOS`, `#Android`

---

<a id="item-2"></a>
## [香港活动家黄之锋因「勾结外国势力」被判囚 10 年](https://www.theguardian.com/world/2026/nov/05/hong-kong-joshua-wong-sentenced-national-security-case) ⭐️ 8.0/10

2026 年 11 月 5 日，香港民主派活动家黄之锋（30 岁）因早前于 9 月承认「勾结外国势力」罪，依据《香港国安法》被判处监禁 10 年。这是黄之锋第二次因《国安法》被定罪，该法由北京于 2020 年 6 月实施。黄之锋自 2020 年起已入狱，是香港唯一一位两度因《国安法》被起诉的活动人士。 10 年重刑显示《国安法》将政治倡议与国际游说纳入刑事范畴，且认罪亦未换来从轻判决，实际上让 2014 年「雨伞运动」及后续抗议的标志性人物在未来十年彻底退出公共舞台。案件亦凸显《国安法》的域外效力：控罪源于黄之锋涉嫌与流亡活动家罗冠聪协调，敦促外国对中国实施制裁。 黄之锋于 2026 年 9 月 2 日认罪，承认与流亡前立法会议员罗冠聪合作，敦促外国政府对中国实施制裁、封锁或其他敌对措施。控方未指控暴力行为，重点在于政治言论与国际倡议。黄之锋自 2020 年首次被捕起即被关押于最高戒备设施。《卫报》独家刊出的狱中信件显示，黄之锋感叹香港命运，但坚守民主理念。

rss · The Guardian - World · 11月5日 15:56

**背景**: 黄之锋 17 岁于 2014 年「雨伞运动」中崭露头角，要求真普选。2016 年他创立民主派组织「香港众志」，该组织在 2020 年 6 月 30 日《国安法》生效数小时后解散。黄之锋首次《国安法》定罪发生于 2021 年，因组织 2020 年 6 月 4 日未经批准集结被判囚 13.5 个月。《国安法》由北京绕过香港立法会强行实施，将分裂国家、颠覆政权、恐怖活动、勾结外国势力列为四大罪行，最高可判终身监禁。

**标签**: `#Hong Kong`, `#national security law`, `#Joshua Wong`, `#pro-democracy`, `#China politics`

---

<a id="item-3"></a>
## [民主党在 2026 年中期选举翻转数十众议院席位，扩大多数优势](https://www.theguardian.com/us-news/live/2026/nov/05/midterm-elections-live-latest-updates-mississippi-senate-race) ⭐️ 8.0/10

2026 年 11 月 3 日举行的美国中期选举中，民主党在俄亥俄州、亚利桑那州和北卡罗来纳州等地翻转数十个众议院席位，将对共和党的领先优势扩大至近 100 个席位。在德克萨斯州参议员选举中，民主党候选人詹姆斯·塔拉里科击败共和党肯·帕克斯顿，成为 1988 年以来首位赢得德州联邦参议员席位的民主党人。共和党参议员泰德·克鲁兹称此次选举为“水门事件级别的否决”。 这波民主党浪潮从根本上重塑国会权力格局，使民主党近乎完全控制众议院，并获得包括历史性德州席位在内的参议院多数，将直接影响贸易、科技限制和对华外交接触等立法优先事项。德州结果显示美国第二大州可能出现政治重组，民主党时隔 38 年再赢参议员席位，表明人口结构变化和经济担忧正在侵蚀共和党统治地位。这一结果增强拜登政府推进其政策议程至 2028 年的能力。 詹姆斯·塔拉里科是前教师，直到 2025 年仍鲜为人知，他以共和党执政下生活成本上升为竞选主轴，胜选时宣称：“我们刚刚夺回了德州”以及“再多的金钱也比不上德州人民的力量”。共和党现任参议员肯·帕克斯顿曾多次与特朗普同台造势，并将塔拉里科描绘为对德州过于进步的候选人。密西西比州参议员选举中，共和党现任辛迪·海德-史密斯与民主党挑战者斯科特·科洛姆得票极其接近，胜负未分。

rss · The Guardian - World · 11月6日 05:36

**背景**: 2026 年中期选举是 2024 年总统大选后首次全国性选举，被视为对拜登政府第二任期表现的公投。历史上总统所属政党在中期选举通常失利，使民主党席位增长极为罕见——上一次总统政党在中期选举中增加众议院席位还是 2002 年小布什时期。德州自 1990 年代以来一直是共和党铁票仓，上一次民主党赢得参议员席位是 1988 年劳埃德·本特森连任。众议院多数门槛为 218 席，近 100 席优势将使民主党获得现代史上最大多数之一。

**标签**: `#US politics`, `#midterm elections`, `#Democrats`, `#House of Representatives`, `#US-China relations`

---

<a id="item-4"></a>
## [英国央行加息 25 个基点至 4% 为 2023 年以来首次](https://news.google.com/rss/articles/CBMisAFBVV95cUxQMUY3RVZDLURQel9mZWtEbWI5aEp6eEEyTU50ck5TOHhTenFuSUhVaGlxX0Z1UHF4cUxxeE1tdTZpMjEzaVlaaUQ2TENfVHVYVndJNWFLclNVemtIaEF0RFBWcE55anJ2cnJYT29jWEk5aHJId2NFOFdvNFBPcTZYTnV4UjhmdHotdm1ITmFNWEt5MVltUjlmOThrbWJXdjU0WEhsWllZRE5aam5WX0w2dQ?oc=5) ⭐️ 8.0/10

英国央行（BoE，英格兰银行）于 2026 年 11 月 5 日将基准利率从 3.75%上调 25 个基点至 4.00%，这是自 2023 年 8 月以来的首次加息。货币政策委员会（MPC）九名成员中有八人支持加息，唯独 Catherine Mann 主张加息 50 个基点。行长 Andrew Bailey 暗示近期可能再次加息，以应对伊朗冲突引发的通胀压力。 加息将进一步推高英国家庭和企业的借贷成本，抵押贷款利率和还款压力在生活成本危机中加剧。作为 G7 央行，英国央行的举动影响全球金融环境，可能推升英镑汇率并冲击包括中国在内的新兴市场资本流动。前瞻指引暗示更多加息，表明央行在衰退风险下仍将抑制通胀置于支持增长之上。 MPC 以 8 比 1 通过加息，Catherine Mann 为唯一反对者并主张半个百分点幅度。《卫报》分析指出加息发生在生活成本危机中，令许多家庭难以置信。美联社报道油价回落可能给英国央行留出更多政策空间。财联社称此次加息符合市场预期。

rss · Reuters \(English\) · 11月5日 20:52

**背景**: 英国央行自 2021 年 12 月从 0.1%开始连续加息至 2022 年底通胀峰值超 11%，于 2023 年 8 月暂停在 3.75%。MPC 法定目标为 2% CPI 通胀，但 2026 年伊朗战争导致供应中断使物价压力再度升温。英国经济在 2023-2024 年勉强避免衰退但增长乏力，央行面临抑制通胀与支持经济的两难选择。

**标签**: `#central banking`, `#monetary policy`, `#interest rates`, `#Bank of England`, `#global finance`

---

<a id="item-5"></a>
## [英伟达 H200 芯片在香港堆积 因中国暂缓进口审批](https://news.google.com/rss/articles/CBMirwFBVV95cUxQZHNUQnlURFBWSTlTSE5wNWUzekR0cDZfcWQzQVRFLVNweXJiSGhtSFZ6cWdvMXF4SHpLRy1YT1Y2QjJZMGxRajNaRGQ1Y25SVGkycEphaU4zTTRJSzV0QjNPTFMxeEl0Mm9CdGFQc0JJTHBNemVoSXdkTnhsR1FNR0t1b2hoUHdfSW0yVnlGMl95Qkd4dDAtMGdhYTFhUzRhc0U1Mm9fdGxLRnhacUNr?oc=5) ⭐️ 8.0/10

路透社 11 月 5 日独家报道，约 60 万颗英伟达 H200 先进 AI 芯片堆积在香港仓库，等待运往中国大陆，因北京方面暂缓大规模进口审批，尽管中国科技企业需求强劲。两名知情人士证实了这一前所未有的积压，凸显中美半导体供应链紧张局势升级。 这 60 万颗 H200 芯片的积压构成中国 AI 发展的关键瓶颈，因这些芯片是训练大语言模型的核心，且 H200 是依据现行美国出口管制合法可对华出口的英伟达最先进 GPU（图形处理器）。审批暂缓显示北京在美对华出口管制下收紧战略技术进口管控，可能拖慢中国 AI 雄心，同时给英伟达带来库存与财务压力——中国市场贡献其营收很大比重。 积压的 H200 为英伟达面向 AI 负载的最新数据中心 GPU，这 60 万颗规模此前未被披露。阿里巴巴、腾讯、字节跳动等中国科技巨头是英伟达合规芯片的主要买家。尽管芯片符合 2023 年 10 月更新的美国出口规则，审批仍被延迟，表明卡点在于中国监管裁量权而非美方限制。

rss · Reuters \(English\) · 11月5日 19:54

**背景**: 自 2022 年 10 月起，美国对华实施升级的半导体出口管制，禁止英伟达顶级 A100 和 H100 芯片对华出口。英伟达随之推出面向中国的 H800 和 A800，2023 年 10 月新规后又推出 H200。香港因独立关税区地位成为关键转运枢纽。中国海关要求先进计算芯片进口许可证，使北京掌握技术流入的节奏与规模主动权。

**标签**: `#US-China relations`, `#semiconductors`, `#trade policy`, `#Nvidia`, `#Hong Kong`

---

<a id="item-6"></a>
## [丁薛祥出席第九届进博会开幕式并提出四大原则促贸易平衡](https://36kr.com/newsflashes/4056829870150789?f=rss) ⭐️ 8.0/10

11 月 5 日，中共中央政治局常委、国务院副总理丁薛祥在上海出席第九届中国国际进口博览会（进博会）暨虹桥国际经济论坛开幕式并作主旨讲话。他针对全球贸易失衡问题提出四点主张：坚持共享市场、深化投资合作、加强创新赋能、增进理解互信。丁薛祥同时表示中国不刻意追求贸易顺差，并指出高科技产品&quot;买不来、不让买&quot;的现状。 作为连续 17 年全球第二大进口国，中国通过进博会释放的政策信号将直接影响全球产供链布局和贸易规则重塑。四大原则旨在以扩大开放和创新合作替代关税壁垒，对跨国企业和&quot;一带一路&quot;共建国家（对华出口占比已达 59.4%）尤为关键。中国全年进口额有望首次突破 3 万亿美元，将重塑大宗商品价格和出口导向型经济体的增长模型。 丁薛祥提出的四大原则具体为：提高开放联通水平发挥比较优势、优化产业跨境布局、提升供给质量拓展贸易边界、通过磋商化解分歧。虹桥论坛首发《出口中国能力发展报告》显示，中国吸纳全球出口比重从 2000 年 3.2%升至 2025 年 9.2%，&quot;一带一路&quot;共建国家对华出口占比达 59.4%，2026 年前 8 个月货物进口额同比增长 26.7%。丁薛祥关于高科技产品&quot;买不来、不让买&quot;的表述直指技术封锁痛点。

rss · 36氪 · 11月5日 20:20

**背景**: 中国国际进口博览会（进博会）自 2018 年创办以来，每年在上海举办，是中国扩大进口、推进双循环战略的国家级平台。虹桥国际经济论坛同期举行，定位高端经贸政策对话机制。中国自 2009 年起连续 17 年稳居全球第二大进口国，全球进口份额从 2000 年 3.2%增至 2025 年 9.2%。第九届进博会召开之际，正值中美科技博弈加剧、世贸组织改革停滞，贸易平衡议题成为各方关注焦点。

**标签**: `#中国经济`, `#进口博览会`, `#丁薛祥`, `#贸易政策`, `#国际经贸`

---

<a id="item-7"></a>
## [前政治局委员马兴瑞因受贿被起诉](https://news.google.com/rss/articles/CBMiakFVX3lxTE0zTkRFZnN4bk5hS0FYWUh1WUpBT3Y2SWhIY2JiUUlsTzhjUnZYM2VPbG9wM25NdnV6SlNRX08tUkZndnpPUE5JUHViLTdFMW90MU1FRGpqOVBBdm83dnZxWnJ6R1NocnFFZ1E?oc=5) ⭐️ 8.0/10

2026 年 11 月 5 日，最高人民检察院（最高检）宣布，中共中央政治局原委员、中央农村工作领导小组原副组长马兴瑞因涉嫌受贿罪、涉案数额特别巨大，经国家监察委员会（国监会）调查终结移送审查起诉，已被依法提起公诉。马兴瑞于 2026 年 4 月 3 日被通报落马，7 月遭“双开”（开除党籍和公职），6 月 26 日其全国人大代表资格被终止。 此案是习近平领导下反腐败斗争的最新高层成果，打击对象为曾主管农村政策、早年长期任职中国航天科技集团公司（航天科技集团）的前政治局委员。马兴瑞涉贪时间跨度超 25 年，从航天科技集团副总经理时期即开始，显示反腐延伸至军工航天系统与农村工作条线，释放“零容忍”持续向纵深推进的信号。 官方指控马兴瑞涉贪跨度超过 25 年，自担任中国航天科技集团公司副总经理时即已开始；他曾任新疆维吾尔自治区党委书记，后晋升政治局委员兼中央农村工作领导小组副组长。最高检已以涉嫌受贿罪对马兴瑞作出逮捕决定，案件将进入法院审判阶段。

rss · 联合早报 · 11月5日 10:10

**背景**: 马兴瑞 1959 年生，长期在航天系统任职，2013-2017 年任中国航天科技集团公司总经理，2017 年调任广东省长，2021 年转任新疆维吾尔自治区党委书记，2022 年 10 月中共二十大上当选中央政治局委员，随后兼任中央农村工作领导小组副组长（该小组统筹全国农业农村政策）。2018 年国家监察委员会成立后，反腐调查权进一步法定化、集中化；马兴瑞案遵循“国监会调查→双开→最高检逮捕起诉”的标准化流程，与近期李小鹏、唐一军等部级高官落马案程序一致。

**标签**: `#中国政治`, `#反腐败`, `#马兴瑞`, `#政治局`, `#法律起诉`

---

<a id="item-8"></a>
## [央视：东风-61 洲际导弹已列装火箭军](https://news.google.com/rss/articles/CBMiakFVX3lxTE5xeXlfTnBiQlZhNGlCa19VYUxEZjZweVV2WjI4RS04T01EeWFma0pjcFpJOC1jbU5ibk1Cc3ViR3MtTVg4SmE1Vll4VThXQ1VPeG9IM1dRX21ZRnVnRzg2YzNPQXlGMlBRLXc?oc=5) ⭐️ 8.0/10

中国中央电视台（央视）于 2026 年 6 月 27 日报道，东风-61（DF-61）洲际弹道导弹已在解放军火箭军开始常态参训，标志着该型号正式列装服役。该消息出现在央视官方账号“小央视频”对火箭军部队多车多弹发射演练的报道中。此前该导弹已于 2025 年 9 月 3 日在北京抗战胜利阅兵中公开亮相，作为陆基机动洲际导弹展示。 东风-61 列装显著提升中国陆基核威慑，增加了可能具备多目标重返大气层飞行器（MIRV）技术和更强生存能力的现代机动洲际导弹，优于老旧的东风-5 井基力量。它与巨浪-3（JL-3）潜射导弹、轰-6N 空基能力共同完成核三位一体现代化，增强北京对美导弹防御的二次打击保证。该部署直接影响印太战略稳定，将纳入美国核态势评估和军控考量。 央视报道使用“东风-61 洲际导弹已常态参训”表述，中方分析人士解读为确认大批量生产已启动且技术指标达标。阅兵中该导弹与巨浪-3、东风-31AG 并列为“战略核导弹第一方队”。《战区》等外媒指出其发射车底盘与东风-41 不同，推测为全新设计而非改进型。

rss · 联合早报 · 11月5日 17:18

**背景**: 中国洲际导弹从液体燃料井基东风-5（1980 年代、射程 1.3 万公里）发展至机动东风-31/31A/31AG 系列，再到东风-41（2019 年阅兵亮相、估计射程 1.2 万公里以上具备 MIRV）。东风-61 为下一代产品，于 2025 年 9 月 3 日抗战胜利 80 周年阅兵首秀。美战略司令部司令安东尼·科顿曾闭门作证称中国在研发超越东风-41 的新型洲际导弹。火箭军 2015 年升格为军种，统管陆基核常导弹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DF-61">DF - 61 - Wikipedia</a></li>
<li><a href="https://web.archive.org/web/20250903005555/https://www.twz.com/nuclear/chinas-new-df-61-intercontinental-ballistic-missile-breaks-cover">China &#x27;s New DF - 61 Intercontinental Ballistic Missile Breaks Cover</a></li>
<li><a href="https://news.qq.com/rain/a/20260627A06CST00">常态 参 训，央视官宣 东 风 61 ...</a></li>

</ul>
</details>

**社区讨论**: 网络讨论集中于东风-61 是全新设计还是东风-41 改进，主流接受官方“全新型号”说法。部分军事观察家质疑“常态参训”表述与正式列装仪式的区别。外文论坛关注其潜在 MIRV 能力对美国本土防御需求的影响。

**标签**: `#军事`, `#国防`, `#导弹`, `#战略威慑`, `#地缘政治`

---

<a id="item-9"></a>
## [中国地方融资平台数量三年半减少逾九成](https://news.google.com/rss/articles/CBMiakFVX3lxTE5Xc3JQY1k2bFZiek8tYkp1Q3NJNjhJTlhPblZjaGlndFRrUDdBdHAtUUZMZ3dNMVk5Y0o2V1V1bmlTN2t1aDdycFNWRjBOQnhJWjB3WjNDMUo2bVdVMWkwLXdiUkx3NXJrV0E?oc=5) ⭐️ 8.0/10

据中国官方披露，截至 2026 年 9 月底，全国剩余地方政府融资平台（LGFV，地方政府融资平台）数量较 2023 年 3 月底减少 92%，三年半时间内数量锐减逾九成，显示地方债务风险化解工作持续推进。 地方融资平台数量锐减 92%标志着中国地方政府融资模式发生结构性转变，直接削减了长期制约财政可持续性和金融稳定的隐性债务风险。平台减少意味着地方政府隐性负债下降、银行体系系统性风险降低，并推动向特殊再融资债券等更透明的预内融资方式转型。 这 92%的降幅覆盖 2023 年 3 月至 2026 年 9 月期间，反映了 2023 年 10 月中央金融工作会议确立的「长效化债机制」落地。各地通过发行特殊再融资债券置换高息短期隐性债务、严控新增平台、推动存量平台通过合并、破产、功能转型等方式退出，实现平台数量大幅压减。

rss · 联合早报 · 11月5日 13:53

**背景**: 地方政府融资平台（LGFV）源于 1994 年分税制改革导致地方财权事权不匹配，2009 年四万亿刺激计划后规模爆发式增长。至 2023 年，LGFV 隐性债务估计达 40-60 万亿元，形成重大财政金融风险。中央随后出台 14 号文、134 号文，确立以政府债券置换隐性债务、实施硬预算约束的化债框架，2023 年 10 月中央金融工作会议进一步明确建立长效化债机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Local_government_financing_vehicle">Local government financing vehicle - Wikipedia</a></li>
<li><a href="https://www.rba.gov.au/publications/bulletin/2024/oct/the-abcs-of-lgfvs-chinas-local-government-financing-vehicles.html">The ABCs of LGFVs: China ’s Local Government Financing Vehicles</a></li>
<li><a href="https://www.chinadaily.com.cn/a/202409/02/WS66d5144aa3108f29c1fc983e.html">Local government debt risks subside on effective resolution moves</a></li>

</ul>
</details>

**标签**: `#地方政府债务`, `#融资平台`, `#金融稳定`, `#财政政策`, `#中国经济`

---

<a id="item-10"></a>
## [美联社独家：特朗普政府战时与伊朗秘密谈判遣返伊朗人](https://news.google.com/rss/articles/CBMipgFBVV95cUxQYmU3cVBtWk1qRjJuVzQzSVFHM190eGl4U1JjOUNZSVpibWNxcVRqallhSVVXLXRnQkxuNzVqWDZMYkpRR2hFd0ltSTNoSlFjMy1uQTlFaE14SGo5cUUtNjV4dXlDUWVBRllwX25sQlFwamh6aGl6Y0tvSm9PWWVvRG5sVG5wQjVWdm1McHhwUlR4bmlmQ0xBZGROSGdyc05wZUlqWURn?oc=5) ⭐️ 7.5/10

特朗普政府在 2025 年 6 月 24 日结束的战争期间，与伊朗举行秘密外交会谈，商讨遣返伊朗国民事宜。美联社获得的法庭文件显示，美国移民与海关执法局（ICE）与伊朗官员协调，于 2025 年遣返了超过 100 名伊朗人，德黑兰对被遣返人员的筛选拥有重大影响力。 这种敌对国家在冲突期间的前所未有的协调，标志着美伊关系的务实转变，可能为未来在核问题或地区安全议题上的谈判打开渠道。在伊朗政府参与下遣返超过 100 人，引发了关于正当程序和陷入地缘政治漩涡的移民待遇的法律与人权担忧。 法庭文件中披露的电子邮件显示，尽管双方关系紧张，伊朗官员对在美国的伊朗移民谁将被遣返拥有重大决定权。据美联社根据解密文件报道，即使战争于 2025 年 6 月 24 日正式结束，首架飞往德黑兰的遣返航班筹备工作仍在继续。

rss · 美联社 · 11月6日 03:22

**背景**: 美国与伊朗自 1980 年以来断绝正式外交关系，特朗普政府退出 2015 年伊核协议（JCPOA）并实施“极限施压”政策后，紧张局势升级。2025 年爆发的直接军事冲突是特朗普第二任期内首次宣战。尽管敌对，双方仍通过后渠道就领事事务保持沟通，包括遣返已用尽法律途径滞留美国的伊朗国民。

**标签**: `#US-Iran relations`, `#Middle East diplomacy`, `#deportation policy`, `#wartime negotiations`, `#geopolitics`

---

<a id="item-11"></a>
## [sshole：通过 crypt\(\) 特殊哈希值绕过 SSH（Secure Shell）认证](https://sshhole.com/) ⭐️ 7.0/10

名为「sshole」的安全漏洞被披露，攻击者可利用 crypt\(\) 函数对特殊密码哈希值（如「\*」和「\!」）的处理方式，绕过 SSH（Secure Shell）认证。该漏洞影响 OpenSSH（开源 SSH 套件）服务器和 musl libc（musl C 库），使攻击者能够登录本应禁用密码登录的账户。漏洞详情发布于 sshhole.com，在 Hacker News（黑客新闻）上获得超过 2,100 分和 529 条评论的高度关注。 该漏洞影响重大，因为 SSH（Secure Shell）是全球 Linux 服务器的主要远程管理协议，众多系统在 /etc/shadow 中使用「\*」或「\!」禁用服务账户的密码认证。此缺陷让攻击者无需有效凭证即可绕过这些控制，可能危及通过 cloud-init（云初始化工具）配置的云镜像及使用 musl libc 的 Alpine Linux（阿尔派 Linux）系统。系统管理员需立即审核带特殊哈希值的账户并应用补丁。 漏洞利用了带内信号缺陷：当 crypt\(\) 接收到「\*」或「\!」等特殊值时，会原样返回输入哈希，导致 \`crypt\(密码, 哈希\) == 哈希\` 比较在任意密码下均成功。musl libc 在 DES（数据加密标准）加密（crypt\_des.c）中已有变通方案，却在 SHA（安全哈希算法）加密（crypt\_sha512.c）中遗漏，使 Alpine Linux 等基于 musl 的发行版面临更高风险。OpenSSH 的 sshd（SSH 守护进程）调用 crypt\(\) 进行密码验证，所有使用受影响 libc 的版本均受波及。sshhole.com 网站提供了概念验证演示。

hackernews · josemrb · 11月5日 20:19 · [社区讨论](https://news.ycombinator.com/item?id=50378228)

**背景**: crypt\(\) 函数是用于密码哈希的标准 C 库函数，通过盐值参数决定算法（如 $6$ 代表 SHA-512）。历史上，Unix 系统在 /etc/passwd 及后来的 /etc/shadow 密码字段使用「\*」或「\!」标记账户为锁定或禁用密码。musl libc 是 glibc（GNU C 库）的轻量级替代品，因体积小、启动快被 Alpine Linux 和众多容器镜像采用。OpenSSH 作为部署最广的 SSH 服务器，依赖系统的 crypt\(\) 实现进行密码认证。crypt\(\) 处理过往曾引发认证绕过漏洞，但特殊哈希值与 musl 不完整变通方案的这种特定交互，似乎是新发现的攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/openssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/">OpenSSH flaw lets attackers log into password -disabled Linux accounts</a></li>
<li><a href="https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/">Security advisory: openssh-server password ... | Alpine Linux</a></li>
<li><a href="https://wiki.musl-libc.org/functional-differences-from-glibc.html">Functional differences from glibc - musl libc</a></li>

</ul>
</details>

**社区讨论**: 社区讨论呈现深度技术分析：用户 mpyne 解释了攻击条件——crypt\(\) 对特殊值原样返回哈希；BoppreH 批评用「\*」等魔法字符串做带内信号；amluto 指出 musl 变通方案不完整（crypt\_des.c 有、crypt\_sha512.c 无）；dabinat 质疑「久经考验更安全」的论点；aljgz 主张「无魔法字符串」设计原则。

**标签**: `#security`, `#ssh`, `#vulnerability`, `#openssh`, `#authentication`

---

<a id="item-12"></a>
## [美国政府警告工业制冷系统面临持续网络威胁](https://techcrunch.com/2026/11/05/u-s-government-warns-of-ongoing-cyber-threat-amid-mass-hacks-of-industrial-retail-and-military-freezers/) ⭐️ 7.0/10

2026 年 11 月 5 日，CISA（美国网络安全和基础设施安全局）、FBI（联邦调查局）、USDA（美国农业部）、HHS（美国卫生与公众服务部）和 DoT（美国交通部）联合发布警告，黑客正在入侵超市、冷库、美军基地及至少一家法国血库的联网工业制冷和冷链监控系统。攻击已波及英国和欧洲至少十几个国家，黑客篡改冷冻温度导致食品变质，安全研究人员将此次攻击归因于伊朗。 冷链基础设施被攻破同时威胁食品安全、医疗物资完整性和军事后勤，造成罕见的跨行业网络物理风险，可能导致大规模库存损失、设备火灾隐患，甚至因血液或药品变质危及生命。警报凸显了像不再获得厂商补丁的 Danfoss（丹佛斯）等老旧运营技术（OT）系统，已成为国家支持黑客组织的首要攻击目标。 联合声明敦促组织将远程管理接口从互联网断开、轮换并加强凭证、应用可用补丁、淘汰生命周期结束的设备。CISA 代理网络安全主管 Chris Butera 表示：「每个依赖制冷和监控系统的组织都应假设自己可能成为目标。」单独的事实页警告，黑客可能强制设备进入持续加热和除霜循环，导致大规模库存损失和设备隐患。

rss · TechCrunch · 11月6日 02:48

**背景**: 工业制冷控制器为远程监控越来越多地接入互联网，但许多运行在已知漏洞的过时固件上。2026 年 10 月，法国超市连锁 Intermarché遭遇 Danfoss 制冷系统网络攻击，导致多家门店运营中断，凸显了 OT 安全鸿沟。CISA 在 2025-2026 年发布多份 ICS（工业控制系统）通报，涵盖 Rockwell、西门子等厂商的关键漏洞，并为关键基础设施运营商提供免费 ICS 网络安全培训。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ic3.gov/CSA/2026/261105.pdf">US Government Partners Urge Hardening Industrial ...</a></li>
<li><a href="https://www.reuters.com/business/retail-consumer/us-warns-ongoing-cyber-threat-industrial-refrigeration-systems-2026-11-05/">US warns of &#x27;ongoing cyber threat&#x27; to industrial ...</a></li>
<li><a href="https://industrialcyber.co/industrial-cyber-attacks/intermarche-cyberattack-exposes-refrigeration-security-risks-as-french-supermarkets-face-operational-disruption/">Intermarché cyberattack exposes refrigeration security risks ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#critical infrastructure`, `#US government`, `#global hacks`, `#industrial systems`

---

<a id="item-13"></a>
## [韩国在美压力下拟扩大海军行动至霍尔木兹海峡附近](https://www.theguardian.com/world/2026/nov/05/south-korea-to-expand-anti-piracy-unit-strait-of-hormuz) ⭐️ 7.0/10

2026 年 11 月 5 日，韩国国防部宣布计划将清海部队（Cheonghae Unit）的作战区域扩展至阿曼杜克姆港（Port of Duqm）附近海域，距离霍尔木兹海峡约 650 公里。政府将向国会提交动议寻求批准，随后还需总统李在明（Lee Jae Myung）和内阁授权。此举是在美总统唐纳德·特朗普（Donald Trump）施压要求韩国支持对伊朗潜在军事行动后作出的决定。 霍尔木兹海峡承担全球约 20%的石油运输量，任何军事升级都直接威胁韩国能源安全——韩国原油进口逾 70%依赖中东。清海部队前移不仅可能将韩国卷入美伊冲突，也显示首尔配合华盛顿「极限施压」政策的姿态。此次部署还将考验韩国宪法对海外军事任务的限制：非联合国授权行动须经国会同意，这在国内可能引发法律与政治争议。 清海部队编制约 300 人，核心舰艇为 4400 吨级忠武公李舜臣级（Chungmugong Yi Sun-sin-class）驱逐舰，自 2009 年起在索马里海域执行联合特遣部队 151（CTF-151）反海盗任务。新授权将使其活动范围延伸至阿拉伯海杜克姆港附近——该深水港是阿曼为规避霍尔木兹瓶颈而建设的战略物流枢纽。路透社报道，进步派议员可能反对动议，理由是超出原反海盗授权范围。国会辩论时间表尚未公布。

rss · The Guardian - World · 11月5日 12:22

**背景**: 清海部队于 2009 年依据联合国安理会决议成立，赴索马里海域执行反海盗护航，每半年轮换一次驱逐舰及补给舰，积累了远海作战经验。2018 年美国退出伊核协议（JCPOA）并恢复对伊制裁后，海湾局势升温，2019-2020 年霍尔木兹海峡附近发生多起油轮袭击事件。2019 年韩国曾以缺乏联合国授权及国内法障碍为由拒绝加入美主导的海上护航联盟。2025 年当选的总统李在明主张外交自主，但面临盟友要求分担防务负担的压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/world/2026/nov/05/south-korea-to-expand-anti-piracy-unit-strait-of-hormuz">South Korea says it will expand naval operations closer to ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cheonghae_Unit">Cheonghae Unit - Wikipedia</a></li>
<li><a href="https://carnegieendowment.org/sada/2026/03/duqm-at-the-crossroads-omans-strategic-port-and-its-role-in-vision-2040">Duqm at the Crossroads: Oman’s Strategic Port and Its Role in ...</a></li>

</ul>
</details>

**标签**: `#South Korea`, `#Strait of Hormuz`, `#naval operations`, `#US-Iran tensions`, `#energy security`

---

<a id="item-14"></a>
## [炸弹威胁扰乱欧洲 15 国 25 余航班](https://www.theguardian.com/world/2026/nov/05/bomb-threats-disrupt-flights-across-europe-and-renew-hybrid-warfare-fears) ⭐️ 7.0/10

2026 年 11 月 5 日星期四，虚假炸弹威胁扰乱了至少 25 个航班，波及意大利、爱尔兰、英国、西班牙、波兰等 15 个欧洲国家，迫使多架航班紧急降落或备降。欧盟交通委员表示目前判断威胁是否协调为时过早，另有报道称一架从米兰飞往华沙的威兹航空航班改降维也纳，一架波兰航空航班降落布鲁塞尔扎文特姆机场。 威胁的规模和地理跨度——同时袭击 15 国——暗示可能是协调行动而非孤立事件，引发对针对欧洲航空基础设施的混合战争战术的严重担忧。扰乱影响数千乘客，并给多国应急响应系统带来压力，展示了低成本威胁如何制造不成比例的混乱和经济损失。 路透社报道至少 27 个客运航班受影响，略高于《卫报》的 25 个统计。意大利通讯社 ANSA 证实两个与意大利相关的航班遭威胁：一架威兹航空米兰-华沙航班改降维也纳，一架芬兰航空赫尔辛基-罗马航班。比利时《晚报》报道一架波兰航空华沙航班降落扎文特姆。欧盟交通委员的谨慎态度与关于俄罗斯混合战争介入的猜测形成对比。

rss · The Guardian - World · 11月6日 02:17

**背景**: 混合战争指融合常规、非正规和网络战术以在公开冲突门槛以下 destabilize 对手，自 2014 年以来俄罗斯常被指控对欧洲目标发动此类行动。此前航空相关混合事件包括 2024 年波罗的海国家上空的 GPS 干扰和 2022 年莱比锡 DHL 货机遭导弹袭击。自 2022 年俄乌冲突升级加剧威胁感知以来，欧盟通过 EASA（欧盟航空安全局）和欧盟委员会交通总司开发协调航空安全响应。

**标签**: `#international security`, `#aviation`, `#Europe`, `#hybrid warfare`, `#transportation disruption`

---

<a id="item-15"></a>
## [也门总统解职部长和军官试图扭转战局](https://www.theguardian.com/world/2026/nov/05/yemen-president-sacks-ministers-and-officers-houthis) ⭐️ 7.0/10

2026 年 11 月 5 日，也门联合国承认的总统解职了多名部长和军事军官，此前胡塞武装在 9 月取得战场胜利，且 10 月 5 日发起的反攻失败，导致双方数千人死亡。此次人事震荡旨在扭转领土损失，并打破持续四周的泰兹围困，泰兹是也门第三大城市。 这次领导层大换血反映出联合国支持的政府在沙特空中优势无法转化为对伊朗支持的胡塞武装的地面战果后的绝望，威胁红海航运通道和地区稳定。人事调整也回应了南方也门派系要求更大权力分享的压力，可能进一步分裂反胡塞联盟。 10 月 5 日的反攻旨在将胡塞武装赶出全国全境，但在激战中崩溃。政府关键盟友沙特阿拉伯面临胡塞武装对其机场和军事基地的近乎每日袭击，同时提供空中支援。截至 2026 年 11 月初，泰兹围困已持续四周。

rss · The Guardian - World · 11月5日 21:47

**背景**: 也门内战始于 2014 年胡塞武装夺取首都萨那，促使沙特领导的联盟于 2015 年干预以恢复联合国承认的政府。据联合国估计，到 2023 年冲突已直接和间接导致超过 37.7 万人死亡，造成全球最严重的人道主义危机之一。伊朗支持胡塞武装，沙特支持政府，使也门成为沙特-伊朗代理人战争的战场。包括 2022 年联合国斡旋停火在内的多次和平努力反复破裂。

**标签**: `#Yemen`, `#Middle East conflict`, `#Houthis`, `#Saudi Arabia`, `#geopolitics`

---

<a id="item-16"></a>
## [伊朗通过卡塔尔向美国提交核提案并附带七项前提条件](https://news.google.com/rss/articles/CBMiywFBVV95cUxOSlJZVlphdWhPcDNGc1E5eDVNdDdMQkJNTXVDS0RYSVRqaC1tblFqQy1FekRQdldnV0FsMU5RdnVHNEI3UEZWMC1MY1l5cnRtcjBlcDlpUXdvX0hXbV91S1UxajV1TEx1VmJ2SzNLNElXSjc3YkdmYWw4VGNXZEl5NXR4RFNjRXBxeEZMLWpBT1Z5X2JRc3NEdkdMZDljQ0dkZXZRbzc3U1NmNkhnaFN5QzNhVmRzSmhsM0Q5VzU3Mm11OWZBa3M1V1lvaw?oc=5) ⭐️ 7.0/10

11 月 5 日，伊朗通过卡塔尔斡旋向美国提交了一份新的核提案，一位伊朗高级官员向路透社证实了这一消息。德黑兰规定，华盛顿必须先满足七项具体要求，随后才能就该提案展开实质性讨论。这一举动标志着在数月间接谈判停滞后，两国敌对关系重新开启外交渠道。 该提案可能重启伊朗核计划外交进程，自 2018 年美国退出《伊核协议》（JCPOA）以来，伊朗核活动大幅扩张，浓缩铀纯度已达 60%。若取得突破将影响全球油价、中东稳定及不扩散体系，失败则可能升级冲突甚至引发以色列军事行动。中国作为《伊核协议》签署国和伊朗主要石油买家，在结果上拥有直接利益。 这位伊朗高级官员表示，提案于周四送达，仅在美方满足伊方七项要求后才会讨论，但具体要求未公开列出。卡塔尔此前曾斡旋囚犯交换及德黑兰与华盛顿的间接对话，确立了可信中介地位。路透社报道发布时，白宫和国务院均未即时回应。

rss · Reuters \(English\) · 11月6日 05:23

**背景**: 2015 年达成的《全面行动联合计划》（JCPOA）以制裁豁免换取伊朗限制核计划，但特朗普 2018 年退出并重启全面制裁。伊朗随即逐步突破限制，将浓缩铀纯度提至 60%——接近武器级——并限制国际原子能机构（IAEA）监查。2021 至 2023 年维也纳间接谈判未能复原协议，国际原子能机构 2024 年报告称伊朗已积累足够 60%浓缩铀，若进一步提纯可制造数枚核武器。卡塔尔曾主办伊美官员秘密外交，包括 2023 年囚犯交换并解冻韩国冻结的 60 亿美元伊朗石油收益。

**标签**: `#Iran`, `#US`, `#nuclear`, `#diplomacy`, `#Middle East`

---

<a id="item-17"></a>
## [美国众院共和党要求英伟达 CEO 就中方间谍指控作简报](https://news.google.com/rss/articles/CBMiywFBVV95cUxNNVFaekphR1ctQUxRQk5CTEFSNnZuTDNJR2FJLUg5UEdXbDZQUEY0UmphZ3JlWFdRLWxDWE4tZjRsQUpPMHhON0lnMTBZdHNocGVfUFJVUHUyd2k1UjlWa1RLQTA5MGh4SlFRUE5heWdZSC1NbkUtMmNrNEJpSHNyV3RFbHoteXZabVk4U0s4dzdoSlhpOWI2aDdSRmtFdk51bjRfOENZaFFrUFQxZDFSUWxOQ21pUHZNZ09fUWJ3Vi1MVW1KTDZVeXFQaw?oc=5) ⭐️ 7.0/10

11 月 5 日，美国众议院资深共和党议员致函英伟达首席执行官黄仁勋，要求他在本月内向国会作简报，回应《纽约时报》上月披露的指控。指控涉及新加坡公司 Megaspeed International 前高管 Alice Huang（黄爱丽丝），她正因涉嫌协助北京获取被禁止出口中国的先进 AI 芯片而接受美国政府调查。 这一国会要求标志着美国对半导体供应链及针对先进 AI 硬件的中方间谍活动审查进一步升级。若指控成立，可能触发对英伟达高端芯片更严格的出口管制，影响其中国营收——在近期限制前，中国约占其数据中心销售额的 20%——并为国会如何监管向对手国家的技术转移树立先例。 路透社看到的信件由众议院外交委员会主席迈克尔·麦考尔和众议院中国问题特别委员会主席约翰·穆伦纳尔牵头签署。《纽约时报》报道称，美国当局正调查总部位于新加坡的 Megaspeed——作为英伟达 AI 芯片买家——是否充当北京获取受限半导体的渠道。英伟达尚未就具体指控公开回应，但此前曾声明其遵守所有适用的出口管制法律。

rss · Reuters \(English\) · 11月6日 02:42

**背景**: 自 2022 年 10 月起，拜登政府对先进 AI 芯片实施了逐步收紧的出口管制——涵盖英伟达 A100、H100 及其中国特供版 A800、H800——以防止此类芯片用于中国军事和监控用途。新加坡已成为关键转运枢纽，美国官员警告当地实体可能将受管技术转运至中国。众议院中国问题特别委员会于 2023 年 1 月成立，将调查技术转移风险和供应链脆弱性列为优先事项。

**标签**: `#US-China relations`, `#technology`, `#Nvidia`, `#espionage`, `#semiconductors`, `#politics`

---

<a id="item-18"></a>
## [伊朗最高国家安全委员会秘书礼萨伊会见普京](https://news.google.com/rss/articles/CBMirAFBVV95cUxQMkR5dEUwb2FoSDZrZ2p1UVF1T3VzbjEwSmhUWFBSeElYM0lHamE3SE0zYVViRHNqZ2piYTBjbWtoZThDU01hQmpYRFlwMHJTTFl3S2MyWnFoZWh1VTRCdEFvckJZcHktYjNpMWxLbU1vOGp3N0k1Yi1FZ0xTMXYzU2I2OHVZeGZrVXdiUmJOZ0phb2dLTjVGTTQ4aGF0WEdOLTVzS2RLQzBYNXR5?oc=5) ⭐️ 7.0/10

11 月 5 日，伊朗最高国家安全委员会（SNSC）秘书穆赫辛·礼萨伊在莫斯科克里姆林宫会见俄罗斯总统弗拉基米尔·普京。礼萨伊转达了最高领袖阿亚图拉·阿里·哈梅内伊的亲笔信函，双方讨论了战后时期的地区安全安排及双边合作。此次会晤发生在伊朗谈判代表刚与调解人就结束与美国敌对状态的提案举行会谈之后。 此次会晤显示在中东局势升温与核外交停滞背景下，伊朗与俄罗斯战略协调进一步深化。俄罗斯的支持增强了伊朗在与美国就制裁解除和地区安全担保进行间接谈判中的筹码。会面也反映出随着西方影响力下降，莫斯科正成为海湾安全架构中更关键的斡旋者。 礼萨伊会后表示：「与普京先生讨论了重要地区议题，并就战后时期和地区安全安排进行了重要对话。」普京办公室证实了克里姆林宫会晤，但未发布具体协议的通报。伊朗官方媒体强调最高领袖信函的传递是此访核心内容。

rss · Reuters \(English\) · 11月6日 02:59

**背景**: 自 2022 年以来，伊朗与俄罗斯扩大了军事与经济合作，包括伊朗向俄罗斯提供无人机用于乌克兰战场，以及在印度洋举行联合海军演习。最高国家安全委员会由总统马苏德·佩泽希齐扬任主席、礼萨伊任秘书，是伊朗最高外交政策协调机构。自美国 2018 年退出《伊核协议》（JCPOA）并恢复制裁以来，伊美紧张关系持续至今。

**标签**: `#Iran`, `#Russia`, `#diplomacy`, `#Middle East`, `#geopolitics`

---

<a id="item-19"></a>
## [幸运咖加盟商向蜜雪集团创始人求援，门店大幅关闭](https://36kr.com/p/4056473489560457?f=rss) ⭐️ 7.0/10

2026 年 2 月，幸运咖加盟商发公开信《致张总：幸运咖加盟商，真的顶不住了！》向蜜雪集团创始人张红超、张红甫求援，称门店亏损难以为继。张红超通过微信回复“（幸运咖）一定会做出改变”，两位创始人随即在年初组织全国巡店，召集亏损加盟商座谈。据 36 氪了解，幸运咖门店数从 2025 年底的 1 万多家回落至 8000 家左右，2026 年上半年日店均营业额仅约 2000 元，折合不足 200 杯，低于盈亏平衡线。 作为曾经门店数仅次于瑞幸、库迪的中国第三大咖啡品牌，幸运咖陷入加盟商亏损、净关店潮，暴露了下沉市场低价咖啡加盟模式的深层困境。8000 家加盟商面临亏损，2026 年全年或持续净关店，考验蜜雪集团上市后统筹双品牌的能力。竞争对手瑞幸咖啡（门店 3 万多家）上半年净增 5000 多家，古茗咖啡收入占比超 20%，双双加码咖啡赛道，进一步挤压幸运咖生存空间。 2025 年蜜雪上市后退出一线管理的张红甫，2026 年亲自带队调研 b³、Ora、肯悦咖啡等竞品。当年加盟商年会上，张红甫当场道歉：“他觉得没有做好，很愧对大家。”幸运咖早期以“奶茶化咖啡”教育市场（美式默认加糖、菜单半数无咖啡因 SKU（库存单位）），2022 年咖啡 SKU 占比提至 70%，首个销售额破亿单品为 2022 年推出的椰椰拿铁。

rss · 36氪 · 11月5日 16:19

**背景**: 幸运咖原为郑州本地精品咖啡品牌，2020 年被蜜雪集团全资收购。蜜雪创始人张红超、张红甫以低调著称，早期从蜜雪冰城抽调核心团队运营幸运咖，定位 5-8 元价格带，主攻三线及以下城市及乡镇——2020 年中国咖啡连锁化率仅 13%，高度集中在一线。幸运咖 2022 年单年从 500 家增至 2000 家，跻身全国规模前三。2025 年蜜雪集团上市后，张红甫逐渐放权退出一线，直至 2026 年危机爆发才重新介入。

**标签**: `#中国商业`, `#咖啡行业`, `#加盟模式`, `#蜜雪集团`, `#幸运咖`, `#消费经济`, `#零售业`

---

<a id="item-20"></a>
## [大众中国转让国轩高科 5.3%股份予合肥国资](https://36kr.com/newsflashes/4056852611339394?f=rss) ⭐️ 7.0/10

大众汽车（中国）投资有限公司拟将持有的 9618.04 万股国轩高科股份（占总股本 5.30%）协议转让给合肥市建设投资有限公司，每股交易价格 24.09 元，转让总价款 23.17 亿元。该事项已获合肥市国资委（国有资产监督管理委员会）批复同意，转让完成后大众中国持股比例将降至 18.98%，合肥建投将成为持股 5%以上股东。 此次交易标志着外资在战略电池企业中的持股比例进一步下降，同时强化了合肥市国资对新能源产业链核心资产的掌控力度。此前大众中国于 2023 年通过定增成为国轩高科第一大股东（持股 26.47%），如今减持至 18.98%并引入合肥建投，反映出地方政府在新能源赛道的深度布局意图。 本次转让价格每股 24.09 元，较国轩高科近期二级市场股价存在折价，总对价 23.17 亿元以现金方式支付。事项尚需取得深交所（深圳证券交易所）合规性确认并办理股份过户登记手续方能生效。大众中国原系通过 2023 年 7 月非公开发行方式取得国轩高科股份。

rss · 36氪 · 11月5日 20:43

**背景**: 国轩高科成立于 2006 年、2015 年在深交所上市，是中国锂电池龙头企业之一，客户涵盖大众等主流车企。2023 年 7 月大众中国斥资 125 亿元定增认购国轩高科 26.47%股份成为第一大股东，并约定放弃部分表决权。合肥市作为安徽省省会，近年围绕江淮汽车、蔚来汽车及国轩高科构建新能源汽车产业集群，市属国企频频入股本地头部企业以巩固产业链控制力。

**标签**: `#新能源汽车`, `#电池`, `#国轩高科`, `#大众汽车`, `#股权转让`, `#合肥国资`

---

<a id="item-21"></a>
## [美国初请失业金人数降至 57 年低位；第三季度生产率飙升](https://news.google.com/rss/articles/CBMiswFBVV95cUxNcm5OTDhuLTE5VENNbUNPODhwRmJyXzBnR1FocDlCWnphSElfTk44Zzl4enh1S1hPUmZsaldReHlNcmVSSVRGTXJFY2Y2TXVmVGVuSlRmQlRGOWg2TV9QQlROV19rank0bG9rX1NIcmlkNWsxcE1KR19XUnhsbFJwdzBMbTgxQ0RLb0JsYy1lQTFkR3VJVkFyel9KeFFCdDNWWE4xeEE4aDNTYmZEejVrcEhPQQ?oc=5) ⭐️ 7.0/10

美国劳工部周四公布的数据显示，截至 10 月 31 日当周经季节性调整后的初请失业金人数减少 6,000 人，降至 18.9 万人，创下自 1969 年以来 57 年新低。同期发布的第三季度非农劳动生产率初值以 2.3%的年化增速增长，超出市场预期的 1.9%，单位劳动成本意外下降 0.8%，为数个季度来首次下降。 历史低位的裁员数据与生产率加速增长的组合表明，劳动力市场依然紧俏但未引发工资推动型通胀，给美联储维持或降息提供了政策空间。单位劳动成本下降缓解了企业利润率压力，降低了工资-价格螺旋上升的风险，这正是美联储实现 2%通胀目标的关键约束条件。 路透社调查的经济学家此前预测初请人数为 21.5 万人，实际值低于预期 2.6 万人，反映裁员力度远低于预期。生产率报告显示，第三季度产出每小时增长 2.3%，单位劳动成本下降 0.8%，而市场预期为上升 0.5%，这一反差强化了软着陆预期。

rss · Reuters \(English\) · 11月5日 23:59

**背景**: 初请失业金人数是美国劳工部自 1967 年起每周追踪的裁员代理指标，上一个 57 年低位为 1969 年 9 月的 18.7 万人。美联储的双重使命要求充分就业与物价稳定；近期数据显示 9 月 CPI（消费者价格指数）同比涨幅回落至 2.4%，而就业依然强劲，引发关于降息节奏的激烈辩论。生产率提升允许工资上涨而不挤压利润或推高通胀，这种动态曾在 1990 年代末扩张期和 2023 年疫情后复苏中出现。

**标签**: `#US economy`, `#jobless claims`, `#productivity`, `#Federal Reserve`, `#economic indicators`

---

<a id="item-22"></a>
## [普京将日本烟草在俄资产置于临时管理](https://news.google.com/rss/articles/CBMixwFBVV95cUxNVlg2TkhyTFdzWm9RWUdLZGwyMXBpWEYyY0VaNEhGdHh5UTdINk1GVW1sU0hJTDU0RkZYMDZMWml4bGw0bjN3S1c2R29lQ1VUdjlxLTdfSm95UU52REFtb0NadDMwNmdvR0NuUjZiWEdfa2R6ckpoRmRRejNDc3NraHNGMFliYXR5Q1ktRkVnQ1pBUEtrX1RTbXF3azQ4QXdsNVVjR01MNWtHQTJVZE9wcnRZc202alhnaHJHaFRTUzV2SkdJdkVj?oc=5) ⭐️ 7.0/10

11 月 5 日，俄罗斯总统普京签署法令，将日本烟草国际（JTI）在俄罗斯制造工厂的股份移交给工业资产股份公司（JSC Industrial Assets）临时管理。这使日本烟草成为最新一家在俄失去本地业务控制权的外国公司。 此次没收升级了克里姆林宫对外国企业资产的控制，向在俄国际投资者发出地缘政治风险加剧的信号。该举措紧随上月日本《北海道新闻》记者今井优树因间谍罪被捕，将企业资产没收与莫斯科-东京外交张力挂钩。 法令专门针对 JTI 在俄罗斯制造工厂的股份，置于工业资产股份公司临时管理之下。俄罗斯外交部指责东京系统性利用记者在俄收集情报，为资产没收提供政治背景。

rss · Reuters \(English\) · 11月6日 00:09

**背景**: 自 2022 年俄乌冲突爆发以来，克里姆林宫多次利用临时管理法令接管外企在俄资产，包括达能、嘉士伯和福腾等。日本烟草国际作为日本烟草株式会社子公司，在俄罗斯运营数十年，是该国烟草行业最大外资纳税企业之一。

**标签**: `#Russia`, `#Japan`, `#Business`, `#Geopolitics`, `#Sanctions`

---

<a id="item-23"></a>
## [伊朗在霍尔木兹海峡袭击油轮 回应美国中期选举](https://news.google.com/rss/articles/CBMirgFBVV95cUxQS25WaGR6RHltaldweFlqblRLWTQwanRGbVY4Vm5YZXBVdUVacG5DSTU3SXd1N00zTDROTTlYaGlnQzZPQUlmeUNPRlExc01kSUUwTFkwQUpWTWlXZEtkdTZmQktpWXUwcGt6dVBHbjkyb25ISjB1N0tOaWNJRHBoNk9iSzBJMURrM2dlemVvVnU5aHplVko3aGlQc296enRpdDlLNWJDWGtLWDZZVWc?oc=5) ⭐️ 7.0/10

11 月 5 日，路透社从迪拜报道，伊朗伊斯兰革命卫队海军宣布，在前 24 小时内有三艘油轮在霍尔木兹海峡遭遇爆炸和起火，德黑兰认定这些船只使用了未经授权的航线。袭击发生在美国 11 月 8 日中期选举前后，伊朗表明只要海湾冲突不解决，航运将持续面临风险。伊朗声称四艘油轮触雷，也门胡塞武装同时宣称对沙特阿拉伯发动导弹袭击，形成双重战线施压。 霍尔木兹海峡承担全球约 20%石油消费量的运输，任何中断都直接威胁全球能源价格和供应链，包括中国——中国原油进口逾 40%来自中东。伊朗布雷袭击与胡塞武装导弹袭击的协同升级，增加了更广泛军事对抗的风险，可能牵涉据报正考虑重新打击德黑兰的美军。穿越海峡油轮的保险费率已飙升，给每桶石油运输增加了可量化的成本。 伊朗革命卫队海军称三艘油轮在周四遭袭，因使用德黑兰视为未经授权的航线，但初步报道未披露船名和船旗。驻巴林的美国海军第五舰队未确认触雷袭击，但表示正密切监控局势。同时，胡塞武装宣称对沙特目标发动导弹袭击，标志着红海侧翼同步升级。油价一度跌向每桶 100 美元，随后因供应担忧回升。

rss · Reuters \(English\) · 11月6日 00:47

**背景**: 自美国 2018 年退出 2015 年《伊核协议》（JCPOA）并重启制裁、重创伊朗石油出口以来，霍尔木兹海峡局势多次升温。2019 年，一系列油轮磁吸水雷袭击和美军无人机被击落曾令双方濒临战争边缘。2022 年 11 月美国中期选举在德黑兰被视为对拜登中东政策的公投，强硬派主张无论美国内政结果如何都必须持续施压。伊朗支持的胡塞武装自 2015 年也门战争爆发以来，多次袭击沙特石油设施。

**标签**: `#Iran`, `#US-Iran tensions`, `#Strait of Hormuz`, `#oil shipping`, `#geopolitics`

---

<a id="item-24"></a>
## [梅洛尼警告欧洲在乌克兰和谈中面临边缘化风险](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPZWEyRHhscmY5cHU0U2FBYTZnMDhyeDJ0YnM3UTgtcnhuaWpuYURrSzhHdUN0eFQwazNPcHIxWEtucTIyX1VSZk9uSzhJN05Vc25HUUZDbEdsaTBpOVJWWFpTZjJJQklwUjYyR2ZOaDlzVUpjWndnTVEzR3RpOWk3TG5qbXVJVUFzT3hHNFFLdWE5c2RMUl9UZ0hETWdMeVoyaGpMRHJGcS1fQQ?oc=5) ⭐️ 7.0/10

意大利总理梅洛尼于 11 月 5 日在罗马举行的新闻发布会上警告，除非欧盟结束分散的外交倡议并指定单一代表，否则欧洲在未来的乌克兰和平谈判中将面临边缘化风险。她呼吁欧盟统一立场，授权一名代表在与俄罗斯和乌克兰的任何谈判中代表整个集团发声。这一表态是在欧洲理事会会议后作出的。 梅洛尼的警告凸显了随着俄乌战争进入第三年，欧盟内部在乌克兰政策上的分歧加剧，这可能削弱欧洲在任何谈判解决方案中的筹码。欧洲立场分裂可能让美国和俄罗斯主导谈判条款，而欧盟缺乏实质性话语权，从而改变地缘政治平衡。她呼吁设立单一特使，反映了意大利在担任 G7 轮值主席国期间推动更协调的欧盟外交政策的意图。 梅洛尼表示：「我深信我们都意识到，呈现出一个四分五裂的欧洲形象，将使欧洲面临被边缘化的风险。」她批评法国和德国等成员国各自为政的平行外交轨道。意大利总理强调，任何和平协议都必须包含对乌克兰的安全保障并尊重国际法。

rss · Reuters \(English\) · 11月5日 21:10

**背景**: 自 2022 年 2 月俄罗斯全面入侵乌克兰以来，欧盟已对莫斯科实施 14 轮制裁，并向基辅提供超过 1000 亿欧元的财政、军事和人道主义援助。然而，成员国在融合步伐、长期安全承诺以及是否支持乌克兰加入北约申请上存在分歧。自 2022 年 10 月上台以来，梅洛尼领导的意大利坚定支持乌克兰，同时主张统一的欧盟外交政策声音。欧洲理事会（欧盟成员国领导人会议）一直难以就乌克兰和平谈判的单一特别代表达成一致。

**标签**: `#World News`, `#Ukraine Conflict`, `#European Politics`, `#Geopolitics`, `#Italy`

---

<a id="item-25"></a>
## [无人机袭击俄罗斯梁赞炼油厂 导致主力装置停运](https://news.google.com/rss/articles/CBMivgFBVV95cUxOWk03bDJPMTdlbGlRNi1YMHRCNHlsMWllWWt4Slk4dEZzeExCbUs5QmtjbG56TzlIWHg2eHZCbEF2U3hucml0UXBIeVoyamdhVlhqWjJTaENueW1tYjdhN1k5dy00NEk3UWJtUG45cmxiOHphOEJkNXJ2dG84UlpFYV8zOWpfMVFnY1dNWVV5Q083Q2VucHFfdG1PeWVtcW9nT216LVJwUlFnbE0wMEhDT3kzVUhnU2NLZ1k2US1R?oc=5) ⭐️ 7.0/10

路透社分析证实，10 月 15 日无人机袭击击中俄罗斯梁赞炼油厂，迫使其 CDU-6 常减压蒸馏装置停运。该厂是俄罗斯最大炼厂之一，袭击后原油加工业务全面中断。近几个月乌克兰无人机已多次袭击彼尔姆、梁赞、塔甘罗格等地炼厂。 此轮袭击延续了 3 月以来的模式：当时约 14%俄罗斯炼能被迫停产，汽油产出下降 12%，国内油价升至半年高点。俄罗斯是中国最大原油来源国，炼厂持续受损可能收紧柴油和燃料油对亚洲出口。袭击深度升级也显示乌克兰打击俄罗斯腹地能源设施能力增强。 业内人士向路透透露，梁赞 CDU-6 装置在 10 月 15 日无人机袭击后停运。7 月 29 日乌克兰无人机曾同步袭击彼尔姆、梁赞、塔甘罗格三地炼厂。路透测算 3 月袭击导致约 14%俄罗斯炼能停摆，汽油产量下降约 12%。

rss · Reuters \(English\) · 11月5日 21:19

**背景**: 2023 年起乌克兰开始用长程无人机系统打击俄罗斯炼厂，旨在削弱军用燃料供应并施加国内政治压力。由罗斯石油运营的梁赞炼厂年处理量约 1700 万吨。2024 年 3 月和 7 月两波袭击迫使多座炼厂临时停工，俄罗斯曾一度禁止汽油出口以稳定内需。

**标签**: `#Russia`, `#Ukraine conflict`, `#energy security`, `#oil refinery`, `#geopolitics`

---


---

**本期模型运行状态：正常** ｜ 主通道 `nvidia/nemotron-3-ultra-550b-a55b:free` 承担 100%。

模型用量：`openai:nvidia/nemotron-3-ultra-550b-a55b:free` 1947k，`openai:deepseek-flash` 1k（合计 1948k tokens）。