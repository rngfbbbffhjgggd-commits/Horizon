---
layout: default
title: "Horizon Summary: 2026-10-28 (ZH)"
date: 2026-10-28
lang: zh
---

> 从 617 条内容中筛选出 25 条重要资讯。

---

1. [EDK2 UEFI 固件严重漏洞威胁全球大多数服务器](#item-1) ⭐️ 8.0/10
2. [胡塞武装称导弹袭击沙特拉斯塔努拉炼油厂](#item-2) ⭐️ 8.0/10
3. [先正达冲刺 660 亿美元估值赴港上市](#item-3) ⭐️ 8.0/10
4. [美军准备在 96 小时内打击伊朗](#item-4) ⭐️ 8.0/10
5. [前证监会（中国证券监督管理委员会）高官王会民因受贿 4.36 亿元被判死缓](#item-5) ⭐️ 8.0/10
6. [反诈博主被柬埔寨电诈头目买凶杀害](#item-6) ⭐️ 8.0/10
7. [前乌克兰军官在汉堡受审 涉嫌破坏北溪管道](#item-7) ⭐️ 8.0/10
8. [巴西货币单日暴跌创 25 年新高 财政忧虑引发市场恐慌](#item-8) ⭐️ 8.0/10
9. [习近平寻求和事佬角色 特朗普另设峰会议程](#item-9) ⭐️ 8.0/10
10. [中国前三季度 31 省 GDP 分化加剧 广东增速首追平全国](#item-10) ⭐️ 8.0/10
11. [前三季度 7.9 万名村官被立案](#item-11) ⭐️ 8.0/10
12. [广电总局禁止 IPTV 开机广告 强制开机全屏直播](#item-12) ⭐️ 8.0/10
13. [2025 年全球太阳能发电量超越核能](#item-13) ⭐️ 8.0/10
14. [美国政府隐瞒关于第 702 条监控权力的秘密 FISA 法院裁决](#item-14) ⭐️ 7.0/10
15. [福特 Fathom 电动皮卡内置双向充电 3 万美元即可实现家庭备用电源](#item-15) ⭐️ 7.0/10
16. [分拆出 Slate Auto 的 Re:Build 完成 21 亿美元融资](#item-16) ⭐️ 7.0/10
17. [CISA（美国网络安全和基础设施安全局）警告关键 PHP 漏洞遭在野利用](#item-17) ⭐️ 7.0/10
18. [美军禁止比亚迪车辆进入冲绳嘉手纳基地](#item-18) ⭐️ 7.0/10
19. [芬兰、挪威领导人致电普京；英国警告北约须备战俄罗斯](#item-19) ⭐️ 7.0/10
20. [以色列大选出口民调显示内塔尼亚胡阵营落后于反对派](#item-20) ⭐️ 7.0/10
21. [两名男子因伊朗关联策划袭击英国皇家空军费尔福德基地被起诉](#item-21) ⭐️ 7.0/10
22. [黑客攻击美国联邦选举委员会（FEC）系统，临近中期选举](#item-22) ⭐️ 7.0/10
23. [FCC（美国联邦通信委员会）批准亚马逊 115 亿美元收购 Globalstar](#item-23) ⭐️ 7.0/10
24. [通用汽车战略转向推出混动 SUV](#item-24) ⭐️ 7.0/10
25. [路透社民调：高通胀将持续至明年全球范围内](#item-25) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [EDK2 UEFI 固件严重漏洞威胁全球大多数服务器](https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/) ⭐️ 8.0/10

研究人员在 2026 年 10 月披露了 EDK2（EFI Development Kit II，EFI 开发工具包第二版）UEFI（统一可扩展固件接口）固件框架中存在的关键代码执行漏洞，攻击者可在服务器启动早期阶段执行任意代码。由于 EDK2 是 UEFI 的参考实现，被主流硬件厂商广泛采用，该漏洞威胁全球绝大多数服务器。修复通过 UEFI 囊式更新（capsule update）分发，可在下一次正常重启时应用，无需立即强制重启。 该漏洞对全球服务器基础设施构成即时严重威胁，因为它能在操作系统加载前的固件层面执行代码，传统安全工具极难检测或缓解。EDK2 支撑着 Intel、AMD、AMI 以及 Dell、HPE、联想等主流 OEM 厂商的 UEFI 实现，几乎所有现代 x86 和 ARM 服务器均可能受影响。启动前执行能力意味着攻击者可植入持久化 Bootkit，即使重装操作系统或更换硬盘也能存活。 漏洞位于 UEFI 启动过程的 DXE（驱动执行环境）阶段，因缓冲区边界处理不当导致缓冲区溢出，可被利用实现任意代码执行。修复仅需配置固件在下次重启时执行 UEFI 囊式更新，管理员可在正常维护窗口安排，无需紧急停机。该漏洞编号为 CVE-2026-6484，继 Eclypsium 于 2025 年 6 月 12 日披露的 Hydrophobia Secure Boot 绕过漏洞之后，凸显了 UEFI 固件弱点的反复出现模式。

rss · Ars Technica · 10月28日 04:25

**背景**: UEFI（统一可扩展固件接口）自 2010 年代初起取代传统 BIOS 成为现代计算机的标准固件接口，由 TianoCore 项目维护的 EDK2 是其主要开源参考实现。UEFI 启动过程包含 SEC（安全）、PEI（预 EFI 初始化）、DXE（驱动执行环境）和 BDS（启动设备选择）等阶段，DXE 阶段负责初始化大多数驱动和协议。固件漏洞极具危害性，因其运行在操作系统（OS，操作系统）和虚拟化层之下，重装系统也无法清除。2022 年 Binarly 研究人员披露 12 个漏洞，可在 Intel、HP、AMI 的 UEFI 实现中实现启动前远程代码执行；2025 年 Hydrophobia 漏洞则展示了影响多厂商的 Secure Boot 绕过技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/coreboot/coreboot/16-payloads-and-external-firmware">Payloads and External Firmware | coreboot/coreboot | DeepWiki</a></li>
<li><a href="https://www.preprints.org/manuscript/202502.1245">Understanding UEFI Capsule Update Mechanisms - preprints.org</a></li>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2026-6484/">CVE-2026-6484: UEFI Firmware RCE Vulnerability - SentinelOne</a></li>
<li><a href="https://eclypsium.com/blog/hydrophobia-secure-boot-bypass-vulnerabilities/">Even More Holes In Your Boot: Critical UEFI Secure Boot ...</a></li>
<li><a href="https://uefi.org/specs/PI/1.8/V2_Overview.html">2. Overview — UEFI Platform Initialization Specification 1.8 ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#vulnerability`, `#UEFI`, `#firmware`, `#servers`

---

<a id="item-2"></a>
## [胡塞武装称导弹袭击沙特拉斯塔努拉炼油厂](https://news.google.com/rss/articles/CBMiwgFBVV95cUxPMU9tRHdmbzQ2ZHlsQzBDVmpqUEhlTk9meXgzN1VMOWlUMnlKOU1ibFRMQ1VQNDNjTkloUG9lb054S2JXZ2YwMS1MMXM4b1pwczl2clNyTHM5RGZVdnd6bzJXTVl4bW4yZ0pGTEV2aEV4dlR2cDNkc0lvNjVMN2ZScklvRDE3S1VyS0FoaC02Z3BqTHJPeTJrekxhM0dONmN0VzdXTmE5QjNfM0pIZ1Q2SHMtSkZzbFNqSThaN2RybDFBdw?oc=5) ⭐️ 8.0/10

2026 年 10 月，也门胡塞武装将战火从边境推进至沙特腹地，并于 10 月 13 日晚袭击沙特阿美位于达曼（达曼靠近拉斯塔努拉炼油厂）的一栋办公楼，引发“有限规模”火灾且无人员伤亡；同日胡塞武装发言人萨雷亚称过去 24 小时内沙特发动约 100 次空袭，本轮冲突累计空袭达 3123 次。 拉斯塔努拉是全球最大炼油厂和出口终端之一，袭击威胁全球能源供应，沙特作为最大石油出口国其设施安全直接影响油价；冲突导致原定 10 月 24 日利雅得举行的欧盟-海合会峰会延期，区域外交受阻；也门人道危机加剧，8 月 1 日至 10 月 17 日新增流离失所超 25 万人，联合国预计 2230 万人需援助。 胡塞武装发言人萨雷亚称 10 月 24 日单日沙特空袭约 100 次，累计 3123 次；10 月 10 日哈立德国王国际机场遇袭致 12 死 309 伤，为 2015 年来最惨重，机场关闭两周后 10 月 25 日才部分恢复；利雅得学校 10 月 11 日至 22 日全面网课；在沙中国人反映回国经济舱机票超 1 万元人民币。

rss · Reuters \(English\) · 10月28日 03:17

**背景**: 也门内战始于 2014 年胡塞武装占领首都萨那，2015 年沙特主导多国联军介入；2022 年联合国斡旋达成停火形成约四年“冷和平”，至 2026 年 10 月彻底破裂。胡塞武装控制以萨那为中心的西北部地区，长期获伊朗政治声援与军事支持；国际承认的也门政府驻亚丁，获沙特联军支持。联合国 2026 年 3 月数据显示 1830 万人面临急性粮食不安全，520 万境内流离失所。

**标签**: `#Yemen`, `#Houthis`, `#Saudi Arabia`, `#oil`, `#energy`, `#Middle East conflict`

---

<a id="item-3"></a>
## [先正达冲刺 660 亿美元估值赴港上市](https://news.google.com/rss/articles/CBMiuAFBVV95cUxOU05UME1TSEswNW42TlplYjA0ek1zMHJibHBnNkUyZWJTZmdpLW04MkhMc3Q0S1JVZzk2OEhyQjhXOEVCQUpMYlZOUW9uMWZCUjVhZW8tVjVwMkpISzRzeGdObW1FU0FHRTl1TTUtdXU0R0dNN3ZSbDJOd2tiTno0c3dXbUlnb3A5N1A3ZnZCZF80MTUtNU9yUm5UYzlicGNGTnhOZncwT2V2UmszNG10emN0SlJiSndS?oc=5) ⭐️ 8.0/10

据路透社 10 月 27 日独家报道，先正达（Syngenta）的顾问团队正在为其在香港的首次公开募股（IPO）争取至少 660 亿美元的估值，上市时间预计在 2025 年初。此次发行拟出售 10%至 20%的股份，由瑞银（UBS）和中金公司（CICC，中国国际金融股份有限公司）联合承销，若成行将成为近年来全球规模最大的 IPO 之一。 若以 660 亿美元定价成行，这将是自 2021 年以来香港最大规模 IPO，也是地缘政治紧张背景下中资跨国企业融资能力的关键测试。募资将主要用于偿还先正达超过 100 亿美元的债务，并支持种子与作物保护业务扩张，直接关联全球粮食供应链稳定；同时也将检验香港作为央企融资枢纽的吸引力。 路透社援引两名知情人士称，瑞银和中金公司正向投资者推介这家总部位于巴塞尔的企业。按 10%至 20%的发售比例计算，融资规模或达 66 亿至 132 亿美元。化工集团（ChemChina）2017 年以 430 亿美元收购先正达，若按 660 亿美元估值上市，隐含增值约 53%。目前尚未正式提交上市申请，时间表仍视市场情况而定。

rss · Reuters \(English\) · 10月28日 00:56

**背景**: 先正达总部位于瑞士巴塞尔，是全球最大的农化与种子企业之一，与拜耳（Bayer）、科迪华（Corteva）和巴斯夫（BASF）并列。中国化工集团（ChemChina）作为央企，于 2017 年完成 430 亿美元收购，创下当时中资海外并购纪录。此后集团推行双重上市策略：2024 年先正达中国业务已在上海科创板上市，此次拟将全球主体引入港交所。自 2021 年以来香港 IPO 市场低迷，融资额大幅萎缩，此次大型发行被视为振兴港股上市热度的关键契机。

**标签**: `#Finance`, `#IPO`, `#Syngenta`, `#ChemChina`, `#Agriculture`

---

<a id="item-4"></a>
## [美军准备在 96 小时内打击伊朗](https://news.google.com/rss/articles/CBMiakFVX3lxTE9Sc19hMXd3cnRZSk0tb0xzZ1ZPM3pSYlJpZ19yaFFBYXpjWE90M19SOExVenJNZVZkT0hoYXVXRG8xd0o4c3Nvcmp0eUtZR1A2aXZsWnR4NnNneWlraUI0Wlk5V1pUbUM5Z0E?oc=5) ⭐️ 8.0/10

据 CNN 引述两名美国官员消息，驻中东美军已做好准备，可在收到特朗普总统命令后 96 小时内对伊朗发动大规模打击，目标涵盖伊朗能源、军事及核设施；但特朗普尚未做出最终决定，且曾多次在最后时刻改变主意。 若美军对伊朗实施大规模打击，将大幅升级中东紧张局势，可能通过霍尔木兹海峡扰乱全球石油供应，并牵涉沙特、以色列等地区大国；冲突亦会使中国在该地区的外交与能源利益复杂化，北京近期已派遣特使前往中东斡旋以防战火蔓延。 沙特、土耳其和巴基斯坦高官周一访问德黑兰与伊朗高层会谈，试图降温；中国外交部证实近期将派特使访问中东等地区；美国国防部已指示中央司令部在数日内完成对伊朗重启大规模军事行动的准备工作，但未给出具体发动日期。

rss · 联合早报 · 10月27日 19:41

**背景**: 美伊紧张关系自 2018 年特朗普政府退出《伊核协议》（JCPOA）并重启制裁后持续升级；先前对抗包括 2020 年 1 月美军击毙伊朗将军苏莱曼尼及伊朗对伊拉克美军基地发动导弹袭击；当前危机源于伊朗数月来的核项目推进及涉及真主党、胡塞武装等代理人的地区冲突。

**标签**: `#国际关系`, `#中东局势`, `#美伊关系`, `#军事冲突`, `#地缘政治`

---

<a id="item-5"></a>
## [前证监会（中国证券监督管理委员会）高官王会民因受贿 4.36 亿元被判死缓](https://news.google.com/rss/articles/CBMiakFVX3lxTFA4VEp2RU8zMUo0aWYzOVA0MHlaVTFQb3pNRTBGWms0X2R3QTRVS2huc1poaEZlMmk4NUFXMTl3bWkzel9XRDlTSjZTNHBIWnA3WnRGc0RuV09HZXV6ckVaLTMyNkdtNlAtMFE?oc=5) ⭐️ 8.0/10

2026 年 10 月 27 日，四川省成都市中级人民法院一审判处中国证券监督管理委员会（证监会）原党委委员、中央纪委国家监委驻证监会纪检监察组原组长王会民死刑，缓期二年执行，因其在 27 年间受贿共计 4.36 亿元人民币。判决同时剥夺其政治权利终身、没收个人全部财产，死缓期满后减为终身监禁、不得减刑假释。 此案创下已公开判决的证监会（中国证券监督管理委员会）系统官员受贿金额最高纪录，远超原发行监管部副主任童道驰的 2.74 亿元、原主席助理朱从玖的 1.05 亿元。重判体现中央对金融监管领域「内鬼」零容忍态度，释放打击利用监管权力谋私的强烈信号。 王会民身兼中央纪委国家监委驻证监会（中国证券监督管理委员会）纪检监察组组长，本应监督反腐却亲自收受巨额贿赂，2025 年 3 月通报指其「执纪违纪、执法犯法、大搞利益交换、大肆收钱敛财」。他于 2025 年 3 月被查、11 月被开除党籍。受贿 4.36 亿元人民币约合 7700 万新元。

rss · 联合早报 · 10月27日 17:28

**背景**: 2023 年以来中国金融领域反腐力度显著加大，证监会（中国证券监督管理委员会）系统已有原副主席王建军、姚刚，原主席助理朱从玖，原发行监管部副主任童道驰等多名高官落马。王会民案件特殊在于其长期担任纪检监察组长，属「看家狗变咬人狗」。成都中院异地审理符合高级别贪腐案件跨区域管辖惯例，避免利益干扰。

**标签**: `#China`, `#anti-corruption`, `#CSRC`, `#finance regulation`, `#judiciary`

---

<a id="item-6"></a>
## [反诈博主被柬埔寨电诈头目买凶杀害](http://www.infzm.com/contents/343525) ⭐️ 8.0/10

2024 年 11 月，反诈博主吴恺（网名「徽剑」）在广东惠州被冒充警察的凶手绑架，凶手受 Telegram 用户「少校」指使、由柬埔寨太子集团骨干刘忍出资 100 万元悬赏。吴恺遭殴打逼迫删除举报文章、最终被踢晕遗弃在江西赣州定南县荒山身亡。2026 年 8 月广东高院终审裁定：主犯赵冰判死缓、13 名同犯获刑，刘忍于 2026 年 6 月被公安部工作组押解回国，但悬赏出资者「少校」至今在逃。 本案揭示境外电诈集团已伸出「黑手」进驻境内：通过非法获取个人信息（「开盒」）与雇凶杀人，直接打击举报人，动摇公众安全感与法治底线。这警示「打击电诈」不能止步境外园区，必须同步斩断境内配套的买凶、窃信、洗钱链条，才能保护敢于发声的公民免受恐惧。 赏金 100 万元由赵冰分得 40 万、陈建华 30 万、陶腾飞等三人各 10 万；赵冰事后经母亲向吴恺养子赔偿 50 万元并获 2025 年 12 月 18 日出具的刑事谅解书。裁定书（2026）粤刑终 68699221 号未披露「少校」真实身份，带走吴恺手机的谢某某仍在逃。刘忍以柬埔寨安徽商会会长身份掩饰赌场暴力放贷、殴打装修老板致死、收保护费、运营电诈园区等犯罪。

rss · 南方周末 · 10月27日 21:25

**背景**: 自 2021 年起中国连续开展「断卡」「断流」专项行动，2023 年更与缅甸、老挝联合打击跨境电诈、遣返数万嫌疑人。电影《孤注一掷》揭示东南亚诈骗园区产业化规模，并隐喻境内存在「线人」。刘忍领导的太子集团即典型新模式：借商会合法外衣掩护武装诈骗园区，并能遥控境内雇凶杀人，显示打击重心必须延伸至境内配套黑产链条。

**社区讨论**: 网友普遍感到恐惧，质疑「以后骂电诈集团还安全吗？」并将案件与《孤注一掷》结尾「电诈分子混入反诈大会」情节对照，认为境内「线人」确凿存在。舆论主流要求继续追缉「少校」、严惩「开盒」与买凶链条，为举报人筑起安全屏障。

**标签**: `#电信诈骗`, `#跨境犯罪`, `#反诈博主`, `#买凶杀人`, `#司法判决`

---

<a id="item-7"></a>
## [前乌克兰军官在汉堡受审 涉嫌破坏北溪管道](https://www.ft.com/content/fdc70b65-af31-4697-91b3-69c6f1a1db9e?syn-25a6b1a6=1) ⭐️ 8.0/10

前乌克兰军官谢尔盖·库兹涅佐夫于 2026 年 10 月 14 日在汉堡汉萨高等地区法院受审，被指控主导了 2022 年 9 月对北溪 1 号和 2 号天然气管道的破坏行动。德国检方指控库兹涅佐夫在乌克兰军方领导层的直接指挥下行事，并提交了其上级的宣誓书作为证据。鉴于案件的地缘政治敏感性，审判在严密安保下进行。 这是欧洲法院首次直接将乌克兰国家机关与北溪袭击联系起来，该袭击切断了俄罗斯通往德国的主要能源动脉，重塑了欧洲能源安全格局。定罪可能损害乌克兰与德国等关键欧洲支持者的关系，同时证实俄罗斯关于乌克兰责任的叙事。判决结果可能影响未来西方军事援助决策及波罗的海地区能源基础设施保护政策。 检方指控库兹涅佐夫指挥一支潜水员小组在波罗的海海床安装炸药，目标为北溪两条管道。据报道，乌克兰军方上级的宣誓书确认了对该行动的直接指挥权。预计审判将持续数月，因潜在报复风险而在高度安保下进行。尚未宣布宣判日期。

rss · FT英文 - World · 10月28日 01:24

**背景**: 北溪 1 号和 2 号管道由俄罗斯天然气工业股份公司所有，于 2022 年 9 月 26 日在丹麦博恩霍尔姆岛附近遭水下爆炸破坏，向波罗的海释放大量甲烷。北溪 1 号自 2011 年起运营，北溪 2 号虽已建成但从未获认证，两条管道均为俄罗斯对德天然气出口的核心通道。德国、丹麦、瑞典的多方调查曾追查包括亲乌克兰游艇团体在内的多种理论，但直至德国提出指控前，未有国家行为体被正式指认。乌克兰始终否认国家层面参与。

**标签**: `#geopolitics`, `#Nord Stream`, `#Russia-Ukraine war`, `#energy security`, `#Germany`

---

<a id="item-8"></a>
## [巴西货币单日暴跌创 25 年新高 财政忧虑引发市场恐慌](https://www.ft.com/content/0231b234-14dc-4ff0-8263-e1063b0a25d5?syn-25a6b1a6=1) ⭐️ 8.0/10

巴西雷亚尔单日暴跌幅度创 25 多年来新高，投资者因担忧总统路易斯·伊纳西奥·卢拉·达席尔瓦的财政管理而大举抛售货币。这次抛售反映出市场对政府坚持支出纪律和债务可持续性的承诺产生深度怀疑。 作为拉美最大经济体和主要大宗商品出口国，巴西的财政稳定直接影响全球粮食和能源市场，其货币动荡可能引发新兴市场传染效应。这场危机还威胁到卢拉为其政治联盟提供支撑的社会项目资金来源。 这次货币崩盘是自 1999 年贬值危机以来最严重的单日表现，但摘要未披露具体跌幅百分比和交易量。市场参与者正密切关注财政部长费尔南多·阿达德团队将推出的具体财政整固措施。

rss · FT英文 - World · 10月27日 21:15

**背景**: 卢拉于 2023 年 1 月重返总统职位，承诺扩大社会支出，但其政府难以通过令金融市场满意的财政规则。巴西公共债务已升至 GDP 的 75%以上，央行维持高利率对抗通胀，造成增长与稳定目标之间的张力。

**标签**: `#Brazil`, `#Currency`, `#Emerging Markets`, `#Fiscal Policy`, `#Lula`

---

<a id="item-9"></a>
## [习近平寻求和事佬角色 特朗普另设峰会议程](https://news.google.com/rss/articles/CBMisgFBVV95cUxPRV84N0VCX2tWQ2VxR000bVZEU29DSXlOa09HZ3VBZzdfOUI0OXFXN3NGSFJYcGlPYkgtYUVjeUJ0ZU9iUE5FZll2TDJ4ekFmNmVmVG13M21WdG8wNnN4ZFFTbVVxTDVJNkM3WDFMQUhFbWJWUmNXcFUxVmpNU3V2S24zQjVIUDVpUGpGc0VjOGZZaGNnSGoxR1ZuZzN5WXhZVzRicUJHRXpjcGE4cDBDMl9R?oc=5) ⭐️ 8.0/10

《华尔街日报（WSJ）》报道，在中国主办亚太经合组织（APEC）峰会前不到一个月，国家主席习近平寻求扮演全球和事佬角色，而美国总统特朗普则为历史性的双边峰会设定不同议程。俄罗斯总统普京提议与特朗普和习近平举行前所未有的三方会晤，增加了外交复杂性。特朗普和习近平在 2026 年已会晤两次——5 月在北京进行第七次会面，9 月在白宫会晤——预计 9 月 24 日将在华盛顿举行第三次会谈。 这种峰会目标的分歧凸显了世界前两大经济体的战略竞争：习近平利用中国作为 APEC 东道主的身份展示全球稳定领导力，而特朗普则利用经济杠杆——要求中国多采购美国农产品和飞机——榨取让步。普京-特朗普-习近平三方会晤可能重塑大国动态，影响乌克兰战争和台海局势下的贸易流向、供应链及印太地区安全架构。 关键细节包括：深圳 APEC 峰会距今不足一个月（预计 2026 年 11 月）；普京的三方会晤提议史无前例；特朗普与习近平 5 月在北京的会晤是双方第七次面对面；习近平国内经济疲软激励其合作；特朗普寻求中国采购美国农产品和飞机的具体承诺；《华尔街日报》指出习近平曾作出类似采购承诺但未完全兑现。下一次峰会定于 2026 年 9 月 24 日在华盛顿举行。

rss · 华尔街日报 · 10月27日 18:55

**背景**: 自 2018 年贸易战以来，中美关系持续恶化，涉及关税、科技管制、台湾问题和人权争端。特朗普首个任期（2017-2021）发起贸易冲突；其 2025 年开始的第二任期通过关税和投资限制延续施压。习近平 2022 年开启第三任期，但面临经济增速放缓、房地产危机和青年失业。2026 年深圳 APEC 峰会是中国自 2014 年北京峰会后首次主办。此前特朗普-习近平会晤包括海湖庄园（2017）、布宜诺斯艾利斯 G20（二十国集团）（2018）和大阪 G20（2019）。2026 年的系列会晤标志着多年后最高层外交的回归。

**标签**: `#中美关系`, `#外交`, `#习近平`, `#特朗普`, `#峰会`

---

<a id="item-10"></a>
## [中国前三季度 31 省 GDP 分化加剧 广东增速首追平全国](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1TWnZBTkswTWJaSWZJLVdSdmMzTUw5VmxmUWxPejFSb2hVbmZhT2thZHJRRW1BNXl0SGpHNDdJUEZ1akZyTllOUTBVaEJkQjdLdGZ0Q2tSYVk4M2ZhZy1JNE9B?oc=5) ⭐️ 8.0/10

财新 10 月 27 日报道，中国 31 个省份已全部公布 2026 年前三季度 GDP 数据，区域经济分化进一步加剧。广东增速自 2022 年下半年以来首次与全国平均水平同步，安徽稳居全国前十；承压省份山西、广西、海南等增速则明显放缓。 分化扩大显示「新质生产力」政策与出口导向型沿海集群优势主要惠及发达地区，资源依赖型及产业单一内陆省份落后差距拉大。这一格局将直接影响中央财政转移支付安排、区域投资决策，以及到 2027 年共同富裕目标的推进节奏。 2026 年上半年西藏以 6.3%增速领跑，浙江 5.7%次之，山东、上海、安徽均为 5.6%，共 15 省跑赢全国均值。广东前三季度增速追平全国，结束连续八个季度低于均值局面。财新归因于新动能加速释放与出口强劲带动珠三角、长三角集群效应。

rss · 财新 · 10月27日 20:57

**背景**: 国家统计局按季发布省级 GDP，2026 年前三季度数据覆盖 1-9 月。2023 年 9 月习近平在黑龙江考察时提出「新质生产力」，强调以科技创新驱动产业升级。广东、浙江、江苏等沿海省份凭借成熟制造集群与出口渠道率先承接政策红利，而山西（煤炭依赖）、广西（边贸依赖）等内陆省份面临结构性阻力，分化趋势自 2024 年起持续扩大。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/%E6%96%B0%E8%B4%A8%E7%94%9F%E4%BA%A7%E5%8A%9B">新质生产力 - 维基百科，自由的百科全书</a></li>

</ul>
</details>

**标签**: `#中国经济`, `#省份GDP`, `#经济数据`, `#地区发展`, `#财新`

---

<a id="item-11"></a>
## [前三季度 7.9 万名村官被立案](https://news.google.com/rss/articles/CBMiX0FVX3lxTE9RNTluWEtKdlJjbWhtRDZVU3BGSy1YN29PZWc0V2lGMUZ3U3NNanFLNlNoUTFydHpfakFrZ2JHVnBTSmp4azhjWjZPQjBFYy0zR2RoUm1iaFVxa0tRc3Fv?oc=5) ⭐️ 8.0/10

中共中央纪委国家监委（中国共产党中央纪律检查委员会和中华人民共和国国家监察委员会）通报，2024 年前三季度共有 7.9 万名现任或原任村党支部书记、村委会主任被立案，这一数字已超过去年全年 6.1 万名的立案总量，较去年同期增加 3 万多人。 立案数激增显示中央加大对农村基层腐败的惩治力度，直接关系到土地征收、集体资产管理、扶贫资金等涉农资金的监管。全国约 60 多万个行政村中，7.9 万名村级一把手被查，反映乡村治理中权力制约机制仍存漏洞，将影响 2025 年乡村振兴战略的落实。 被立案对象为现任或原任村党支部书记、村委会主任，即行政村的一把手。单季度数据显示一季度即达 2.3 万人，三个季度持续高位。中央纪委国家监委暂未公布按违纪类型或地区的分类统计。

rss · 财新 · 10月27日 15:06

**背景**: 自 2021 年起，中央纪委国家监委单独公布村级干部立案数，不再并入&\#x27;农村、企业等其他人员&\#x27;大类。2022 年和 2023 年全年均为 6.1 万人，2024 年前三季度即达 7.9 万，显示打击力度明显升级。重点整治土地征收、集体资产交易、惠农补贴发放等村支书、村主任掌握较大自由裁量权的&\#x27;微腐败&\#x27;领域。

**标签**: `#反腐败`, `#基层治理`, `#村官`, `#中国政治`, `#民生`

---

<a id="item-12"></a>
## [广电总局禁止 IPTV 开机广告 强制开机全屏直播](https://www.nrta.gov.cn/art/2026/10/27/art_1588_74296.html) ⭐️ 8.0/10

国家广播电视总局（广电总局）于 2026 年 10 月 27 日发布《交互式网络电视运营服务管理暂行规定》，自 2026 年 11 月 27 日起施行。新规要求 IPTV 集成播控服务提供者实现开机看全屏直播功能，设置频道回看入口，不得播放开机广告；智能电视机应支持优先呈现直播频道功能，遥控器需实现一键切换直播信源。 新规直接回应数亿 IPTV 用户对强制开机广告、遥控器操作复杂、收费不透明的长期投诉。强制设立免费专区并明示收费信息，将降低家庭意外支出，简化老年群体的观看体验。直播优先原则在流媒体冲击下强化了广播电视的公共服务属性。 第十一条规定 IPTV 须实现开机全屏直播、设频道回看入口、禁播开机广告；第十二条要求提供便捷设置入口供用户自选开机进直播或交互主页；第十三条强制首页设免费专区、精简收费栏目、明示收费信息、规范应用专区订购支付。酒店等集团用户亦须遵守直播优先原则。

telegram · zaihuapd · 10月27日 13:59

**背景**: 中国 IPTV 用户规模已超 3 亿户，由各省广电网络在广电总局监管下运营。多年来用户诟病开机广告长达 30-60 秒且不可跳过、进入直播需按 5-10 次遥控器、自动续费缺乏明确授权。广电总局 2021 年和 2023 年曾发文督促改善体验，但属非强制性指导。本次暂行规定首次以法律约束力确立具体技术指标与明确施行期限。

**社区讨论**: 网络讨论显示公众强烈支持禁播开机广告和简化遥控器，大量用户吐槽现有 IPTV 体验。业内人士指出中小省级运营商落地难度大、广告收入损失或致订阅费上涨。部分用户担心运营商通过涨价转嫁广告损失。

**标签**: `#China`, `#IPTV`, `#regulation`, `#consumer rights`, `#technology policy`

---

<a id="item-13"></a>
## [2025 年全球太阳能发电量超越核能](https://www.solidot.org/story?sid=85725) ⭐️ 8.0/10

根据能源智库 Ember（能源智库）的数据，2025 年全球太阳能发电量首次略微超过核能发电量。截至 2026 年 9 月的 12 个月滚动期内，太阳能发电量已比核能高出 13%。2025 年全球电力需求增量的四分之三由太阳能满足，自 2000 年以来太阳能发电量增长约 2700 倍，而核能发电量基本保持不变。 这一里程碑标志着太阳能成为历史上增长最快的电力来源和全球能源转型的核心引擎，牛津大学教授 Jan Rosenow 指出太阳能已是能源转型的引擎。自 2020 年成为最便宜电力来源后，巴基斯坦太阳能占比从 2019 年不足 2% 跃升至 24%、非洲每天安装约 10 万块电池板等案例，显示出从化石燃料和核能向分布式可再生能源的结构性转移。 澳大利亚已有逾 400 万户家庭安装屋顶太阳能系统。电池储能对于将白天太阳能发电转移至晚间用电高峰至关重要。BBC Future 于 2026 年 10 月 23 日发表的文章详细记录了太阳能如何通过成本下降和政策支持超越核能。

telegram · solidot · 10月27日 23:30

**背景**: 太阳能光伏技术在 2010 年左右达到商业成熟，经历数十年发展。国际能源署（IEA）在 2020 年宣布太阳能成为历史上最便宜的电力来源。十年前太阳能仅占全球发电量 1%，预计 2026 年份额将达 10%。核能虽提供稳定基荷电力，但面临高成本、建设周期长以及福岛事故（2011 年）后公众反对等挑战。

**标签**: `#Solar energy`, `#Nuclear energy`, `#Energy transition`, `#Renewable energy`, `#Climate change`

---

<a id="item-14"></a>
## [美国政府隐瞒关于第 702 条监控权力的秘密 FISA 法院裁决](https://www.wired.com/story/the-us-government-is-hiding-a-secret-court-ruling-about-how-it-spies-on-americans/) ⭐️ 7.0/10

《连线》杂志报道，美国政府正在隐瞒一份外国情报监视法院（FISC，外国情报监视法院）的机密裁决，该裁决解释了《外国情报监视法》（FISA，《外国情报监视法》）第 702 条的监控权力。参议员罗恩·怀德（Ron Wyden，罗恩·怀德）警告称，这一被多届政府依赖的秘密法律解释，在最终解密时会让美国民众&quot;震惊&quot;。该裁决涉及政府如何利用第 702 条权力实施影响美国公民的监控。 这一秘密裁决削弱了国会的监督和公众对监控权力的辩论，因为议员们在不知情的情况下重新授权了第 702 条。这种隐瞒影响了数百万美国人的隐私权，他们的通信可能在第 702 条针对海外外国人的定向监控中被&quot;附带收集&quot;。这代表了 9·11 事件后通过秘密法律授权绕过传统搜查令要求、扩大监控权力的趋势延续。 怀德参议员在 3 月表示：&quot;当它最终解密时，美国人民会震惊于这花了这么长时间，以及国会在信息不足的情况下辩论这项权力。&quot; FISA 法院在保密状态下运作，其裁决属于机密，第 702 条最近于 2024 年 4 月获得重新授权。尽管怀德多次要求，政府拒绝解密该裁决。

hackernews · helterskelter2 · 10月27日 22:06 · [社区讨论](https://news.ycombinator.com/item?id=50259604)

**背景**: 第 702 条于 2008 年通过《外国情报监视法修正案》加入 FISA，允许无需搜查令收集合理认为位于美国境外的非美国人通信，以获取外国情报。自 2013 年斯诺登（Snowden，斯诺登）揭露其范围以来，该项目备受争议，包括从互联网骨干网的&quot;上游收集&quot;和从科技公司的&quot;PRISM（棱镜计划）&quot;收集。外国情报监视法院（FISC）批准年度认证，但其意见保持机密。第 702 条于 2024 年 4 月在关于 FBI 查询美国人数据的激烈辩论后获得重新授权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Foreign_Intelligence_Surveillance_Act">Foreign Intelligence Surveillance Act - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2024/04/12/us/politics/surveillance-law-section-702-fisa.html">What is FISA , and What Does It Mean for U.S. Surveillance and...</a></li>
<li><a href="https://www.npr.org/2024/04/20/1246076114/senate-passes-reauthorization-surveillance-program-fisa">Biden signs reauthorization of surveillance program into law... : NPR</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了对秘密法院和两党监控共识的深度怀疑。用户指出美国宣称自由与大规模国内监控的矛盾，提及 Lavabit 和斯诺登等过往揭露，并认为秘密法院从根本上与民主不兼容。有人指出大规模监控的技术基础设施（后门、光纤窃听）早已存在，却缺乏实质性的政治挑战。

**标签**: `#US surveillance`, `#Section 702`, `#FISA court`, `#government secrecy`, `#digital privacy`

---

<a id="item-15"></a>
## [福特 Fathom 电动皮卡内置双向充电 3 万美元即可实现家庭备用电源](https://arstechnica.com/cars/2026/10/ford-builds-bidrectional-charging-into-its-30k-electric-truck/) ⭐️ 7.0/10

福特发布售价 30,000 美元的 Fathom 电动皮卡，内置双向充电硬件可向家庭输出 10 kW 功率，无需单独的壁挂式逆变器。该系统需搭配福特新款 Home Backup Panel（家庭备用电源面板），成本比首代 5,000 美元面板降低约 60%。含车辆、电源系统（约 2,255 美元）及面板的完整套装起价约 32,200 美元。 此举让车辆到家庭（V2H，Vehicle-to-Home）备用电源大幅降价并普及，免去了单独安装逆变器的费用。约 32,200 美元的系统总成本低于特斯拉 Powerwall 等专用家庭电池，同时兼具交通与储能功能。福特首年销量目标超 10 万辆，将使其成为美国市场销量最高的具备 V2H 功能的电动汽车（EV，电动汽车）。 Fathom 内置逆变器可在停电时向家庭持续输出 10 kW 功率。新款 Home Backup Panel 定价约 2,000 美元，较首代 5,000 美元面板降低 60%。电源系统组件约 2,255 美元。据报道，福特首年销量目标超 10 万辆，这一数量是除特斯拉外美国市场单一电动汽车从未达到的纪录。

rss · Ars Technica · 10月28日 00:17

**背景**: 双向充电（V2G/V2H，Vehicle-to-Grid/Vehicle-to-Home）让电动汽车电池可向家庭或电网放电，日本已强制要求电动汽车具备该功能，全球普及度正在提升。此前福特 F-150 Lightning 等车型实现 V2H 需单独购买 5,000 美元逆变器并安装面板。Fathom 将逆变器集成至车内，降低了硬件成本与安装复杂度。中国电动汽车厂商将 V2G/V2H 作为全球竞争优势大力推广。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vehicle-to-grid">Vehicle -to-grid - Wikipedia</a></li>
<li><a href="https://www.tesla.com/learn/bidirectional-charging-vehicle-to-home">Bidirectional Charging 101: Vehicle-to-Home - Tesla</a></li>

</ul>
</details>

**标签**: `#Electric Vehicles`, `#Bidirectional Charging`, `#Vehicle-to-Home`, `#Ford`, `#Energy Storage`

---

<a id="item-16"></a>
## [分拆出 Slate Auto 的 Re:Build 完成 21 亿美元融资](https://techcrunch.com/2026/10/27/rebuild-which-spun-out-slate-auto-raises-2-1b/) ⭐️ 7.0/10

马萨诸塞州制造加速器 Re:Build Manufacturing 周二宣布完成 21 亿美元融资，由 General Catalyst 和 JPMorganChase 战略投资集团领投。该公司 2023 年分拆出电动车初创公司 Slate Auto，表示将用资金扩大硬科技产品制造能力并孵化新工业初创企业，以确保创新产品能在美国本土生产。

rss · TechCrunch · 10月28日 04:31

**背景**: Re:Build Manufacturing 由前 Amazon（亚马逊）商业 CEO Jeff Wilke 与 Miles Arnone 于 2020 年创立，采用混合模式：既与工业企业合作在航空航天和国防领域大规模设计制造，又孵化服务不足关键市场的初创公司。高管团队多来自 Amazon（亚马逊），包括长期担任 VP 兼 Jeff Bezos（杰夫·贝佐斯）技术顾问的 Wei Gao。其「美国版深圳」定位指向深圳密集的电子制造生态——零部件供应商、装配线与工程人才聚集，支撑硬件快速迭代，而美国自 2000 年代去工业化加速后基本丧失该能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/20140817060936-1391-shenzhen-trip-report-visiting-the-world-s-manufacturing-ecosystem">Shenzhen trip report - visiting the world&#x27;s manufacturing ecosystem</a></li>
<li><a href="https://venturecapitaltracker.com/glossary/hard-tech">What Is Hard Tech? | Venture Capital Tracker</a></li>
<li><a href="https://manufacturingaccelerator.org/">Home - Manufacturing Accelerator</a></li>

</ul>
</details>

**标签**: `#manufacturing`, `#funding`, `#US-China competition`, `#EV industry`, `#supply chain`

---

<a id="item-17"></a>
## [CISA（美国网络安全和基础设施安全局）警告关键 PHP 漏洞遭在野利用](https://techcrunch.com/2026/10/27/us-government-says-hackers-are-now-exploiting-critical-php-web-bugs/) ⭐️ 7.0/10

2026 年 10 月 27 日，美国网络安全和基础设施安全局（CISA）确认黑客正在积极利用两个关键 PHP 漏洞（CVE-2024-4577 和 CVE-2024-4578），并命令所有联邦文职机构在三天内（即 10 月 30 日前）完成修补。PHP 约占全球面向 Web 服务器的 70%，潜在受影响范围极广。 PHP 运行在全球约 70% 的网站上，这两个远程代码执行漏洞的在野利用使数百万站点面临数据泄露、勒索软件和服务中断风险。AI 辅助研究在两年内解锁了原本被认为‘无法利用’的漏洞利用链，标志着老旧开源基础设施中沉睡的缺陷现在可被快速武器化，改变了威胁格局。 这两个漏洞被命名为 ‘PHP2Shell’，两年前被发现但被判定无法利用，直到 2026 年初安全公司 Calif 借助 AI 模型将其串联成可用利用代码。PHP 于 10 月 20 日左右发布补丁；CISA 的强制性运营指令要求联邦机构最晚在 10 月 30 日前修补。部分政府和大型企业已预防性下线站点。CVE-2024-4577 CVSS 评分 9.8（严重），CVE-2024-4578 评分 8.4（高危），均影响 Windows 上的 PHP CGI 模式，自 2024 年 6 月起已被用于投放远控木马、挖矿程序和 DDoS 僵尸网络。

rss · TechCrunch · 10月27日 22:40

**背景**: PHP 是支撑全球约 70% 网站的数十年老牌开源脚本语言，其核心维护依赖资金有限的非营利基金会，难以负担专职安全审计。两个漏洞位于 Windows 上的 PHP CGI（通用网关接口）模块，利用 Best-Fit 字符编码注入参数实现无需认证的远程代码执行。CVE-2024-4577 绕过了十多年前修补的 CVE-2012-1823 同类缺陷。自 2024 年 6 月起已有多个威胁组织在野利用，投放 XMRig 挖矿程序、Mirai 变种等恶意软件。此次事件凸显了资源不足的关键开源软件构成的系统性风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.csa.gov.sg/alerts-and-advisories/alerts/al-2024-067/">Critical Vulnerability in Hypertext Preprocessor ( PHP ) Software</a></li>
<li><a href="https://www.sentinelone.com/vulnerability-database/cve-2024-4577/">CVE-2024-4577: PHP CGI on Windows RCE Vulnerability - SentinelOne</a></li>
<li><a href="https://www.fortiguard.com/outbreak-alert/php-rce-attack">PHP RCE Attack | Outbreak Alert | FortiGuard Labs</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#PHP`, `#vulnerability`, `#CISA`, `#web security`

---

<a id="item-18"></a>
## [美军禁止比亚迪车辆进入冲绳嘉手纳基地](https://www.theguardian.com/world/2026/oct/27/us-bans-byd-electric-vehicles-kadena-military-base) ⭐️ 7.0/10

美军驻日部队于周二宣布，自本周起禁止中国电动汽车制造商比亚迪（BYD）生产的车辆进入位于冲绳的嘉手纳空军基地，禁令同时适用于进入基地的送货司机和出租车。此举被视为华盛顿打击涉嫌收集敏感情报的中国技术的更广泛行动的一部分。 这一禁令预示着美国可能在全球军事设施扩大对中国技术的限制，直接针对全球销量最大的电动汽车制造商。这可能加速汽车供应链的脱钩，并为其他驻有美军基地的美国盟友树立先例。此举凸显了美国对联网中国汽车在敏感设施附近运行可能带来的数据安全风险的日益担忧。 禁令于本周在嘉手纳空军基地生效，该基地是美国最大的海外军事基地之一。限制不仅针对军事人员，还涵盖进入基地的民用送货司机和出租车。美军称比亚迪车辆构成「不可接受」的安全风险，但未披露具体技术漏洞。官员表示类似措施可能在其他美军设施实施。

rss · The Guardian - World · 10月27日 10:50

**背景**: 冲绳嘉手纳空军基地驻扎约 1.8 万名美军人员，是美军在印太地区的关键空中力量枢纽。比亚迪于 2023 年超越特斯拉成为全球销量第一的电动汽车制造商，并已拓展至日本等海外市场。美国此前以间谍担忧为由限制中国电信设备（华为、中兴）和 TikTok。配备传感器、摄像头和数据链路的联网汽车日益被视为潜在情报收集平台。根据美日安全条约，日本驻扎超过 5 万名美军人员，分布于多个基地。

**标签**: `#US-China relations`, `#BYD`, `#military security`, `#electric vehicles`, `#Japan`

---

<a id="item-19"></a>
## [芬兰、挪威领导人致电普京；英国警告北约须备战俄罗斯](https://www.theguardian.com/world/live/2026/oct/27/russia-ukraine-oleshky-serbia-france-europe-latest-news-updates) ⭐️ 7.0/10

2026 年 10 月 27 日，芬兰总统亚历山大·斯图布和挪威首相约纳斯·加尔·斯特勒与俄罗斯总统弗拉基米尔·普京举行了实质性电话会谈，讨论乌克兰和平谈判。与此同时，英国国防大臣韦斯·斯特里廷警告称，普京正在考验北约（北大西洋公约组织）的决心，联盟必须为可能与俄罗斯爆发战争做好准备，并引用普京在 2022 年入侵乌克兰前给出的虚假保证作为佐证。 两个北欧北约成员国直接与普京接触，标志着战争爆发以来罕见的欧洲外交主动，但其他欧洲领导人的怀疑态度凸显了对话能否见效的分歧。斯特里廷明确警告北约须为与俄罗斯开战做准备，显示西方威慑姿态趋于强硬，也凸显了外交努力若失败可能引发升级的风险。 斯特里廷表示：「并非因为我们想要战争——我们与俄罗斯人民无仇无怨……但当普京保证无意挑起与北约的战争时，我们想起了他在入侵乌克兰前几天对乌克兰所说的话。」他还称赞波兰是「我们在欧洲最伟大、当然也是最可靠的朋友之一」。卫报直播博客还提到，在美方斡旋协议下无人机袭击停止后，俄罗斯炼油厂提高了产量；德国总理默茨坚持认为，俄罗斯和美国不能在没有基辅和欧洲参与的情况下解决战争。

rss · The Guardian - World · 10月28日 00:23

**背景**: 自 2022 年 2 月俄罗斯全面入侵乌克兰以来，普京与西欧领导人的直接联系极为罕见，大多数沟通通过中介进行。芬兰和挪威分别于 2023 年和 2024 年加入北约，结束了数十年的中立政策，使北约北翼直接与俄罗斯接壤。英国一直是乌克兰主要军事援助提供国，并持续主张强化北约威慑姿态。此前的和平倡议，包括 2022 年伊斯坦布尔会谈和多项停火提议，均未能达成持久解决方案。

**标签**: `#Russia-Ukraine war`, `#NATO`, `#diplomacy`, `#peace negotiations`, `#UK defence`

---

<a id="item-20"></a>
## [以色列大选出口民调显示内塔尼亚胡阵营落后于反对派](https://www.theguardian.com/world/live/2026/oct/27/israel-elections-knesset-netanyahu-likud-eisenkot-gaza-latest-updates) ⭐️ 7.0/10

2026 年 10 月 27 日发布的出口民调显示，由前以色列国防军（IDF）参谋长加迪·艾森科特（Gadi Eisenkot）领导的反对派阵营在以色列议会（Knesset）选举中以微弱优势领先总理本雅明·内塔尼亚胡（Benjamin Netanyahu）的右翼联盟。利库德集团（Likud）成为最大单一政党，但反对派联盟预计总席位更多。本次选举投票率创历史新高，阿拉伯裔以色列选民参与度创纪录，数万名海外以色列人专程飞回国内投票。 这是 2023 年 10 月 7 日哈马斯（Hamas）袭击以来的首次全国大选，被视为对内塔尼亚胡安全教条及其极右翼联盟处理加沙战争方式的公投。若反对派主导组阁，可能改变以色列在人质谈判、约旦河西岸（West Bank）定居点政策以及与美国及阿拉伯邻国关系上的立场。阿拉伯裔选民投票率激增预示以色列政治版图可能重组，影响未来数年权力平衡。 10 月 7 日遇难者家属在特拉维夫「人质广场」于上午 6 时 29 分默哀一分钟，该时刻正是哈马斯发动袭击的时刻，呼吁选民铭记损失。早期迹象显示巴勒斯坦政党席位增幅最大。以色列法律要求公民亲自到场投票，仅外交官等极少数例外。最终联盟组成仍不明朗，因两大阵营均未明显跨过 61 席半数门槛。

rss · The Guardian - World · 10月28日 06:33

**背景**: 以色列议会制要求在 120 席的议会（Knesset）中获得 61 席多数才能组阁。内塔尼亚胡累计担任总理 16 年，最近一次自 2022 年底起领导包含极右翼和极正统派政党的联盟。2023 年 10 月 7 日袭击造成约 1200 名以色列人死亡，引发持续至今的加沙战争，据加沙卫生部门统计已致超 4 万巴勒斯坦人死亡。2019 至 2021 年间曾举行四次无果选举，随后内塔尼亚胡重掌大权。

**社区讨论**: Reddit 上《卫报》直播帖的评论显示两极分化严重：部分用户欢庆内塔尼亚胡时代可能终结，另一些人担忧艾森科特阵营因中间派、左翼与阿拉伯政党理念差异难以组建稳定联盟。多位评论者指出阿拉伯裔选民创纪录投票率将改变以色列民主的未来走向。

**标签**: `#Israel`, `#election`, `#Netanyahu`, `#Middle East politics`, `#exit polls`

---

<a id="item-21"></a>
## [两名男子因伊朗关联策划袭击英国皇家空军费尔福德基地被起诉](https://www.theguardian.com/uk-news/2026/oct/27/two-men-charged-raf-fairford) ⭐️ 7.0/10

2026 年 10 月 27 日，英国威斯敏斯特治安法院审理了两名男子根据《国家安全法案》被起诉策划袭击格洛斯特郡皇家空军费尔福德基地的案件。检方指控该阴谋由一名化名「阿里」的操纵人协调，警方认为其为伊朗情报机构工作，曾指使五名男子于 2026 年 9 月 27 日驾驶装满汽油的货车前往该基地。 此案是依据 2023 年《国家安全法案》首次因伊朗指使的在英阴谋而提起的起诉，标志着伊朗与英国紧张关系可能升级。费尔福德基地部署有美国 B-52 轰炸机且为北约关键资产，成为攻击目标凸显了关键军事设施面临国家支持的恐怖主义威胁。 五名受雇司机之一于 9 月 27 日凌晨在操纵人警告车内有炸弹后报警，从而挫败了阴谋。两名被告于 2026 年 10 月 27 日出庭威斯敏斯特治安法院，但首次聆讯未披露其身份。

rss · The Guardian - World · 10月28日 03:24

**背景**: 位于格洛斯特郡的皇家空军费尔福德基地是欧洲唯一的美军重型轰炸机基地，常驻 B-52 和 B-2 轰炸机执行北约演习任务。英国 2023 年《国家安全法案》新增外国干涉和破坏罪名，取代旧法以应对不断演变的国家威胁。自 2018 年以来，伊朗伊斯兰革命卫队（IRGC）被牵连至欧洲多起针对异见人士和西方目标的阴谋，包括 2022 年挫败的巴黎伊朗反对派集会袭击案。

**标签**: `#UK`, `#Iran`, `#national security`, `#terrorism`, `#geopolitics`

---

<a id="item-22"></a>
## [黑客攻击美国联邦选举委员会（FEC）系统，临近中期选举](https://news.google.com/rss/articles/CBMiuAFBVV95cUxPbDV3WWJ5Ulh3Q05tT203WGNGVE1UNmFvZ2ZoclFXemtrWXFhNlRhUmtabmlPZXRaYU1sQ251VWhSSWJMODNJQkRrMk9MNFdfb1RVT2VJQTR4akpfM0JQNk9wMkpMV2tFY2tHc2ZpTGMwcHlLNFU3UDBrZk5MbGFrb2ZqX25XRVZCQmI5Z29LbDI5cjF2S0JodjVNcVVmV3RyUFR1SW5RZUwwY2JlSWJrRUMyNEgta3dl?oc=5) ⭐️ 7.0/10

2022 年 10 月 27 日，黑客攻击了美国联邦选举委员会（FEC，Federal Election Commission）网站，导致其电子申报系统瘫痪，距离 11 月 3 日中期选举仅剩一周。路透社根据一封内部邮件独家披露，此次攻击使竞选团队无法提交法定的竞选财务报告。当时 2022 年中期选举已成为美国历史上最昂贵的选举周期，政治广告追踪机构 AdImpact 统计广告支出约达 112.1 亿美元。 此次针对联邦选举委员会（FEC）申报系统的攻击直接威胁竞选财务透明度，可能让选民在投票前无法知晓候选人资金来源。在广告支出高达 112.1 亿美元的历史最贵中期选举中，系统瘫痪引发对外国干预或国内行为体试图掩盖资金影响力的担忧。事件凸显美国选举基础设施的脆弱性不仅限于投票机，还延伸至监管政治资金的联邦机构。 根据路透社看到的邮件，联邦选举委员会（FEC）的电子申报系统因攻击下线，委员会未立即确认数据是否泄露或攻击者身份。攻击发生在竞选团队面临 10 月 27 日选前报告申报截止日期之际，给候选人和政治行动委员会带来合规风险。AdImpact 统计的 112.1 亿美元广告支出凸显了 FEC 系统旨在追踪并向公众披露的巨额资金流向。

rss · Reuters \(English\) · 10月28日 05:24

**背景**: 联邦选举委员会（FEC）成立于 1975 年，是负责执行联邦竞选财务法（包括政治捐款和支出披露要求）的独立监管机构。其电子申报系统每个选举周期处理数百万笔交易，是公众了解美国政治竞选资金来源的主要窗口。2022 年中期选举因激烈的参议院和众议院竞争创下支出新高，自 2016 年俄罗斯干预大选以来，FEC 已警告选举基础设施面临更多网络威胁。此前曾发生 2020 年投票软件供应商遭勒索软件攻击事件，但这是首次已知直接针对 FEC 自身披露平台的攻击。

**标签**: `#US politics`, `#cybersecurity`, `#elections`, `#FEC`, `#midterms`

---

<a id="item-23"></a>
## [FCC（美国联邦通信委员会）批准亚马逊 115 亿美元收购 Globalstar](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNU2pZY3J4T2Fvd0hub09FM2RkaHJQc21pOWRWal80cHpZMXN2RS1La2M2WmpVY1hnbzlnUHNBZG5rQ3hWTFZPdmh0cmFPMHVHV0ttRlhzXzZ2SVdFOTd5ZU42YWFTblZtQnRPQUZNcENPSWJUeEF2TE5JRFFXaUdCRlZmLUFCT1JhT0wxWGpKNlZXYnowUG52dlBqc1JYS2EwcE1PS3gwVzhhYWZ4RkJURTh0LWl6SWxEOVIzT3RXbG1EZw?oc=5) ⭐️ 7.0/10

美国联邦通信委员会（FCC）已批准亚马逊 Leo 以 115 亿美元收购卫星运营商 Globalstar，允许亚马逊将 Globalstar 约二十余颗低地球轨道卫星整合进其 Project Kuiper（柯伊伯计划）星座。该交易于 2026 年 4 月首次宣布，FCC 太空局同时批准 Globalstar 的 C-3 系统进入美国市场，扩展了亚马逊的直连手机（D2D）卫星连接能力。 该批准加速了亚马逊挑战 SpaceX Starlink 在卫星宽带领域主导地位的步伐，通过获得 Globalstar 现有的轨道资产和宝贵的 L 频段与 S 频段频谱许可——这对无需专用终端即可连接普通智能手机的直连手机（D2D）服务至关重要。同时也增强了亚马逊在快速增长的 D2D 市场中的地位，该市场预计到 2034 年将达到 32.6 亿美元，复合年增长率 24.7%；Globalstar 与苹果合作为 iPhone 提供紧急卫星消息服务，提供了即时收入来源和技术基础。 交易对 Globalstar 估值约 115 亿至 116 亿美元，将增加约 24 颗运行在 1,414 公里高度的卫星，补充亚马逊计划部署 3,236 颗卫星的 Kuiper 星座。FCC 批准紧随太空局授予 Globalstar 非地球同步 C-3 系统美国市场准入。分析师警告，收购无法解决亚马逊的火箭发射瓶颈，Kuiper 仍依赖 ULA、蓝色起源和阿丽亚娜空间有限的发射运力来部署完整星座。

rss · Reuters \(English\) · 10月28日 04:49

**背景**: 亚马逊 Leo 成立于 2019 年作为 Project Kuiper（柯伊伯计划）子公司，目标在低地球轨道部署超过 3,200 颗卫星提供全球宽带，直接竞争 SpaceX 已拥有 6,000 多颗在轨卫星的 Starlink 星座。Globalstar 作为美国老牌卫星运营商，自 2000 年代初起维护 24 颗 LEO 卫星提供语音和低速数据服务，近期在日本、西班牙和德州扩建地面网络支持下一代 C-3 星座。该公司自 2022 年起与苹果合作，在 iPhone 14 及后续机型上实现卫星紧急 SOS，验证了直连手机技术的可行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kuiper_Systems">Amazon Leo - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Globalstar">Globalstar - Wikipedia</a></li>
<li><a href="https://www.fortunebusinessinsights.com/direct-to-device-satellite-connectivity-market-118206">Direct To Device Satellite Connectivity Market Size, Share [2034]</a></li>

</ul>
</details>

**标签**: `#Amazon`, `#Globalstar`, `#satellite communications`, `#M&amp;A`, `#Project Kuiper`

---

<a id="item-24"></a>
## [通用汽车战略转向推出混动 SUV](https://news.google.com/rss/articles/CBMikAFBVV95cUxQSEJFVWVjR3Y2ekp3X2hVSGVuOHplSWZiT296X3c0QnlWV2NQd1BfTjRqOFJNbGhLWk00cEJ2MERfUlJfQndsU2FFcGh6dTZTcFh0bUpWdlpaeUJUZ0VJMWRreFZ1YURfQndSc3Y2SkxsTklkNXNlNE9tanpjSVRZZWtWN290aTFIcXh5STh6RGs?oc=5) ⭐️ 7.0/10

通用汽车（GM）于 10 月 27 日宣布将为其三款热门三排座 SUV——雪佛兰 Traverse、GMC Acadia 和别克 Enclave——推出混合动力版本，标志着该公司从纯电动战略的重大转向。此前通用曾大力投资纯电动汽车（BEV）并完全放弃混动技术路线。 这一转向反映出汽车行业普遍认识到消费者对全面电动化的接受速度低于预期，混动成为务实的过渡技术。作为拥有上汽通用合资企业的全球最大车企之一，通用的战略调整将影响全球产品规划，并重塑中国——全球最大汽车市场——的竞争格局。 混动车型将瞄准利润丰厚的三排座 SUV 细分市场，通用在该领域占据强势地位。路透社援引知情人士消息称这是重金押注纯电后的战略调整，但首份报道未披露具体上市时间表或技术参数。

rss · Reuters \(English\) · 10月28日 02:53

**背景**: 通用此前承诺到 2035 年实现新款轻型车零尾气排放，并投入数十亿美元建设 Ultium 电池平台与电动车产能。但美国电动车普及速度不及预期，混动车型因成本更低、续航更长且不依赖充电桩而市场份额上升，倒逼通用调整策略。

**标签**: `#automotive`, `#electric vehicles`, `#hybrid vehicles`, `#General Motors`, `#business strategy`

---

<a id="item-25"></a>
## [路透社民调：高通胀将持续至明年全球范围内](https://news.google.com/rss/articles/CBMiswFBVV95cUxQSGlkNFRUdUxnaVVWLTVGV2pJeEdyQzVIUTBoak15M0dBVjMzcGZrV0NjMnVISDZud2U2RGdDcXc3NUZpSU5QNGtSS0xpc2F3QkR0Y05OOE00czlTSUV6ZUQ1V1Vrdk9BT2x6Qzk1a1IycThjeEJ0bk5MT3FjN0FxTEpvdFV1aEZ6MkRfTkJpbVU5eEZVdlhOVzdxVkJENXpjazlRVk0yZlROcTByLVluVXp0MA?oc=5) ⭐️ 7.0/10

路透社于 10 月 27 日在班加罗尔发布的数百名经济学家民调显示，高通胀将在全球经济中持续至明年。经济学家们越来越担心，价格压力将在能源成本上涨之外变得根深蒂固。 持续的高通胀限制了央行降息空间，影响美国、欧元区和英国等主要经济体的货币政策。对中国而言，全球通胀持续推高进口成本、削弱出口竞争力，同时压缩国内支持增长的政策空间。 英国央行和欧洲央行均警告可能进一步加息，巴西央行因油价较 3 月预测上涨 25%而上调通胀预期。该民调反映出通胀正从暂时性向结构性转变的日益担忧。

rss · Reuters \(English\) · 10月27日 23:47

**背景**: 自 2021 年以来，主要经济体面临数十年来最高通胀，由疫情供应链中断、财政刺激及 2022 年俄乌冲突引发的能源冲击驱动。央行激进加息应对，美联储将利率从近零提至 2023 年的 5%以上。虽通胀已从峰值回落，但多数发达经济体核心指标仍高于目标，引发对‘最后一公里’去通胀最艰难的争论。

**标签**: `#global economy`, `#inflation`, `#Reuters poll`, `#monetary policy`, `#economic outlook`

---


---

**本期模型运行状态：正常** ｜ 主通道 `nvidia/nemotron-3-ultra-550b-a55b:free` 承担 100%。

模型用量：`openai:nvidia/nemotron-3-ultra-550b-a55b:free` 3984k，`openai:deepseek-flash` 0k（合计 3984k tokens）。