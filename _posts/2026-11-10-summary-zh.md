---
layout: default
title: "Horizon Summary: 2026-11-10 (ZH)"
date: 2026-11-10
lang: zh
---

> 从 670 条内容中筛选出 25 条重要资讯。

---

1. [允许黑客通过 SSH 登录 Linux 设备的漏洞正被积极利用](#item-1) ⭐️ 8.0/10
2. [英伟达董事会调查黄仁勋涉嫌与中国间谍关系](#item-2) ⭐️ 8.0/10
3. [法国指责伊朗革命卫队（伊斯兰革命卫队）发动超市冷柜网络攻击，誓言实施欧盟制裁](#item-3) ⭐️ 8.0/10
4. [特朗普在白宫宣布美伊战争「实际上已结束」](#item-4) ⭐️ 8.0/10
5. [乌克兰袭击俄炼油厂导致多地燃油短缺](#item-5) ⭐️ 8.0/10
6. [中国银行上调美元存款利率以平抑人民币升值](#item-6) ⭐️ 8.0/10
7. [中国将对美贸易休战延长两个月](#item-7) ⭐️ 8.0/10
8. [药明康德获美国国防部从 1260H（2021 财年国防授权法案第 1260H 条）中国军工企业名单移除](#item-8) ⭐️ 8.0/10
9. [特朗普预计在华 APEC 峰会会晤习近平和普京](#item-9) ⭐️ 8.0/10
10. [太原豪生公寓火灾致 14 死 喷淋系统失灵](#item-10) ⭐️ 8.0/10
11. [英飞凌（Infineon）实现全球首个 300 毫米碳化硅功率器件](#item-11) ⭐️ 7.0/10
12. [Fervo Energy 获得 120 亿美元增强型地热系统订单](#item-12) ⭐️ 7.0/10
13. [美国国防部长赫格塞斯本周面临众议院弹劾投票](#item-13) ⭐️ 7.0/10
14. [波音因生产困境裁减商用飞机部门 5%员工](#item-14) ⭐️ 7.0/10
15. [沙特东西向输油管线在麦地那地区遭袭](#item-15) ⭐️ 7.0/10
16. [FDA（美国食品药品监督管理局）强制要求 Ozempic 和 Zepbound 增加眼部风险警示](#item-16) ⭐️ 7.0/10
17. [泽连斯基在俄乌谈判前与莫迪通话](#item-17) ⭐️ 7.0/10
18. [礼来口服减重药 Foundayo（福达ヨ）后期试验显著改善睡眠呼吸暂停](#item-18) ⭐️ 7.0/10
19. [欧盟（European Union）外交负责人卡拉斯指责俄罗斯假装谈判实则轰炸平民](#item-19) ⭐️ 7.0/10
20. [比亚迪仰望在阿布扎比全球首发鼎曜超豪华轿车 预估售价 200 万元](#item-20) ⭐️ 7.0/10
21. [特朗普政府推动永续期货进入美国市场，华尔街老牌机构敲响风险警钟](#item-21) ⭐️ 7.0/10
22. [中国将稀土出口管制暂停期延长至 1 月](#item-22) ⭐️ 7.0/10
23. [南非选民在地方选举中拒绝 ANC（非洲人国民大会）多数席位](#item-23) ⭐️ 7.0/10
24. [阿联酋加尔加什警告地区长期不确定性，称美伊和解前景艰难](#item-24) ⭐️ 7.0/10
25. [孟加拉临时政府拒绝谢赫·哈西娜护照申请](#item-25) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [允许黑客通过 SSH 登录 Linux 设备的漏洞正被积极利用](https://arstechnica.com/security/2026/11/vulnerability-that-lets-hackers-ssh-into-linux-devices-is-under-active-exploitation/) ⭐️ 8.0/10

名为“sshole”的漏洞允许攻击者通过 SSH 登录运行 OpenSSH 且基于 musl libc 的 Linux 发行版（包括 Alpine Linux、OpenWrt 和 Buildroot），这些系统默认禁用 PAM 认证却启用密码认证。CISA 已将其列入“已知被利用漏洞”目录，Cisco 于 2026 年 11 月初确认发现活跃利用。

rss · Ars Technica · 11月10日 03:41

**背景**: Alpine Linux 是基于 musl libc 与 BusyBox 的安全导向轻量级发行版，因约 5 MB 体积成为容器镜像主流选择。musl libc 是精简、符合标准的 C 库，未实现 glibc 的大多数区域设置功能。PAM（可插拔认证模块）提供模块化认证框架；Alpine 的 openssh-server 包默认禁用 PAM，直接使用密码验证。这一特定组合构成了 sshole 利用的攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alpinelinux.org/">index | Alpine Linux</a></li>
<li><a href="https://musl.libc.org/">musl libc</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linux_PAM">Linux PAM - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#Linux`, `#SSH`, `#vulnerability`, `#active exploitation`

---

<a id="item-2"></a>
## [英伟达董事会调查黄仁勋涉嫌与中国间谍关系](https://techcrunch.com/2026/11/09/the-race-is-on-to-sue-nvidia/) ⭐️ 8.0/10

英伟达董事会于 2026 年 11 月 8 日周日宣布启动独立调查，针对首席执行官黄仁勋与一名被指向北京传递情报的中国女商人的关系。消息公布后英伟达股价下跌逾 4%，且《纽约时报》（NYT）已于 10 月 29 日报道称特朗普在 2025 年曾获情报简报知悉此事。路透社同日披露英伟达及黄仁勋因相关披露问题已面临股东诉讼。 此调查动摇全球市值最高芯片公司的领导层稳定性，英伟达 GPU（图形处理器）主导的 AI 算力供应链对中美科技产业均至关重要。公司早前将相关担忧称为&quot;正常&quot;的表态可能构成证券法违规，法律专家预警将引发高昂股东诉讼，路透社已报道相关集体诉讼启动。案件加剧中美科技博弈，可能影响出口管制执行，因黄仁勋长期主导英伟达对华业务谈判。 特朗普于 11 月 9 日周一表示已与黄仁勋通话，并称联邦调查局（FBI）&quot;正在调查&quot;，同时表达同情称黄仁勋&quot;正承受煎熬&quot;。埃隆·马斯克（Elon Musk）及多位金融大佬公开声援黄仁勋，路透社确认英伟达及黄仁勋因披露问题已被起诉。英伟达股价在调查宣布后单日跌幅超 4%，市值蒸发数百亿美元，后续董事会能否完成继任规划成为焦点。

rss · TechCrunch · 11月10日 06:23

**背景**: 英伟达成立于 1993 年，黄仁勋自创立以来担任 CEO，凭借 GPU（图形处理器）在 AI 训练与推理中的核心地位，于 2024-2025 年成为全球市值最高半导体企业。自 2022 年美国实施先进芯片对华出口管制以来，黄仁勋亲自参与与政策制定者的博弈，力求在合规与保持中国市场份额间取得平衡。据 10 月情报简报，涉案中国女商人被认定为情报人员，长期通过建立人脉网络接近美国科技高管以获取敏感信息。美国情报机构在向特朗普过渡团队通报前，已对该关系持续监控至少一年，显示国家安全层面的高度重视。

**标签**: `#Nvidia`, `#Jensen Huang`, `#US-China relations`, `#AI chips`, `#securities law`

---

<a id="item-3"></a>
## [法国指责伊朗革命卫队（伊斯兰革命卫队）发动超市冷柜网络攻击，誓言实施欧盟制裁](https://www.theguardian.com/world/2026/nov/09/france-blames-irans-revolutionary-guards-for-cyber-attacks-on-supermarket-fridges) ⭐️ 8.0/10

法国外交部长让-诺埃尔·巴罗（Jean-Noël Barrot）正式将 2026 年 10 月 11 日至 12 日针对法国及欧洲多国超市制冷系统的大规模网络攻击归咎于伊朗伊斯兰革命卫队（IRGC）。攻击者劫持丹佛斯（Danfoss）数字恒温器，强制启动 50°C（122°F）除霜循环，导致数百家欧洲超市价值数百万欧元的食品库存报废。巴罗誓言实施&quot;全欧洲范围制裁&quot;，并将此次行动定性为&quot;前所未有的规模和前所未有的侵略行为&quot;。 这标志着国家支持的网络战归因显著升级：北约成员国直接指责伊朗军事分支攻击对食品药品供应至关重要的民用冷链关键基础设施。协调一致的欧盟制裁威胁可能重塑伊朗-欧洲外交关系，并为集体应对工业物联网破坏确立先例。该事件还触发了美国网安基础设施安全局（CISA）、联邦调查局（FBI）、卫生公共服务部（HHS）、农业部（USDA）和交通部（DOT）于 2026 年 11 月 5 日发布的联合预警，凸显联网制冷控制器的全球脆弱性。 攻击利用管理工业制冷的丹佛斯 SCADA/OT 控制器，于 2026 年 10 月 11 日至 12 日深夜强制启动除霜操作。美国多机构于 2026 年 11 月 5 日发布联合事实页，敦促运营商加固暴露在公网的控制器。与革命卫队有关的伊朗&quot;网络复仇者&quot;组织曾于 2023 年入侵以色列 Unitronics 水控系统，并通过深度伪造视频劫持阿联酋电视流媒体播报加沙战争虚假新闻。法国调查推定超市攻击与欧洲其他类似事件有关联。

rss · The Guardian - World · 11月10日 01:54

**背景**: 伊朗伊斯兰革命卫队（IRGC）至少自 2023 年起通过&quot;网络复仇者&quot;等组织开展网络行动，瞄准以色列制造的工业设备和海湾媒体。攻击利用制冷领域的联网工业控制系统（ICS/SCADA），该领域在欧盟（NIS2 指令）和美国均被列为关键基础设施。法国和欧盟自 2019 年起建立网络外交工具箱，可对恶意网络活动实施制裁。冷链监控系统守护对温度敏感的食品、药品和血液供应，使其成为高价值破坏目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servnetuk.com/news/scada-ot-cyberattack-danfoss-refrigeration-2026">Danfoss Refrigeration Hack 2026: UK OT Security Lessons</a></li>
<li><a href="https://www.ic3.gov/CSA/2026/261105.pdf">US Government Partners Urge Hardening Industrial ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#international relations`, `#Iran`, `#France`, `#sanctions`

---

<a id="item-4"></a>
## [特朗普在白宫宣布美伊战争「实际上已结束」](https://www.theguardian.com/us-news/2026/nov/09/trump-iran-war) ⭐️ 8.0/10

2026 年 11 月 9 日，美国总统特朗普在白宫新闻发布会上表示，美伊战争「实际上已结束」，此前他刚与卡塔尔首相举行会谈。他淡化了中期选举后美军升级对伊军事行动的担忧，称以色列和海湾盟友已受到良好保护，无需进一步升级。 这一表态标志着一场扰动全球能源市场的中东重大冲突可能结束，特朗普讲话后油价在盘后交易中已下跌逾 7 美元/桶。这种转变可能稳定影响中国能源安全和「一带一路」海湾投资的地区安全格局，同时也会改变美国在该地区的军事承诺。 特朗普表示战争结束将「很快到来」，并强调无需军事升级。油市即时反应，盘后交易价格下跌超 7 美元/桶。国务卿鲁比奥单独表态称对伊战争「不一定受欢迎」，但为阻止核威胁所必需；伊朗提出为期两天的和谈框架，据报道已被美方拒绝。

rss · The Guardian - World · 11月10日 06:58

**背景**: 美伊冲突在 2025-2026 年显著升级，美军直接打击伊朗核设施及地区代理武装。卡塔尔作为关键调解方，主持了美伊间接谈判。2026 年 11 月中期选举给特朗普政府带来降级压力，而伊朗核计划突破 2015 年《伊核协议》（JCPOA）限制仍是核心冲突起因。中国原油进口逾 40%来自中东，地区稳定对其能源安全至关重要。

**标签**: `#US-Iran relations`, `#Middle East conflict`, `#Trump administration`, `#geopolitics`, `#energy markets`

---

<a id="item-5"></a>
## [乌克兰袭击俄炼油厂导致多地燃油短缺](https://news.google.com/rss/articles/CBMivwFBVV95cUxPcnFSWF9iWmo0LUNjUmNYMVVKYzBwNVlJdlJsbVkxWnJ1Z2NYckF0OFFFdUNwdVZqd1VESWdzbEdRQmF6VGliV0tpYmVvNE9nS2l5LVczdWNhVXZjT0hTTTlnMzNIWnV2LS1nQWNKRGlYNzdUMkV1V3NabzVNUkhmWENLblNYRGJCUTJhMEVXU1dYXzU2Z1YxdTUycDZqNEFVbGRJZVlKOS0zaEcwVEdOZWZCbTR5VFIzaGhWZGZFZw?oc=5) ⭐️ 8.0/10

乌克兰武装部队在过去两周内袭击了至少八座俄罗斯主要炼油厂，包括俄罗斯第二大炼油厂基里希（Kirishi）工厂，导致燃油短缺再次蔓延至至少六个俄罗斯联邦主体。地方政府已实施汽油和柴油限购配给，从克里米亚到莫斯科的俄罗斯石油（Rosneft）加油站前均出现排队加油车龙。 新一轮炼厂打击正值克里姆林宫依赖能源收入维持战争机器之际，威胁俄罗斯国内燃油供应，并可能收紧本已平衡的全球柴油与汽油市场。作为俄罗斯原油主要买家，中国若面对俄罗斯炼厂长期停工，成品油出口流向与东北亚定价均可能发生改变。 路透社 11 月 9 日报道，官方与俄媒证实，两周袭击潮后至少半打联邦主体出现短缺。由俄罗斯石油（Rosneft）运营、日处理量约 34 万桶的基里希炼厂在最新袭击中受损，业内分析师估算早期打击已使全国汽油产量下降 10%-15%。

rss · Reuters \(English\) · 11月9日 19:41

**背景**: 乌克兰自 2024 年初起系统打击俄罗斯能源设施，利用长程无人机攻击纵深数百公里的炼厂、油库与泵站。至 2024 年中，此类袭击导致俄罗斯数十年来最严重汽油荒，迫使莫斯科禁止汽油出口六个月并在重点设施部署防空系统。2026 年底供应刚现脆弱复苏，11 月 2 日乌克兰重启打击，显示其旨在持续削弱俄罗斯炼能与出口创汇能力的战略意图。

**标签**: `#Russia-Ukraine war`, `#energy security`, `#geopolitics`, `#global oil markets`, `#China-Russia relations`

---

<a id="item-6"></a>
## [中国银行上调美元存款利率以平抑人民币升值](https://news.google.com/rss/articles/CBMiywFBVV95cUxQTzF1MFhueDRWX1A3LWlGYWJuZ21hMjNBQkE5aG9JdElOT1pYeUNrMHUxS2lXaGQ4RDAxUUp1T256bjBXelZMZ3UyNDA1UEI5QlJ4SHgwX3QweWsyczBnRUhRTC1PZGtpRUVFNzVycWp3d1RQVE0zUm40SUNURVdES2EwZmpNUFNlMGV5S1lXajlza3A4OW1RSGFzWldtU1N1N0N1R0kxbTUxRGtXU29FX0x3M2J6SU5yVjBxWk1yZmN2WHdvR01UMGtqaw?oc=5) ⭐️ 8.0/10

中国国有大行在北京指令下上调美元存款利率，旨在放缓人民币对美元升值。此举源于 2024 年 6 月份中小银行率先提高美元存款利率，迫使大型国有银行跟进以免流失美元资金。主要国有银行目前人民币存款利率仅为 0.95%，使美元存款更具吸引力。 这一政策转向直接影响持有逾 1 万亿美元外币存款的中国储户，可能将资金从人民币资产转向美元资产。通过提高美元存款吸引力，北京旨在增加在岸市场美元供给，缓解人民币升值压力——后者因美联储降息预期而走强。这标志着从此前央行（PBOC）要求将 5 万美元以上美元存款利率上限限制在 4.3%的政策逆转。 消息人士称，中小银行于 2024 年 6 月率先上调利率，迫使大型国有银行被迫跟进竞争。主要国有银行目前人民币存款利率仅 0.95%，而此前央行（PBOC）指导将 5 万美元以上美元存款利率上限限制在 4.3%。中国银行据报将吸收的美元资金投向美债，以在低国内收益环境下获取更高收益。

rss · Reuters \(English\) · 11月9日 13:36

**背景**: 中国通过央行（PBOC）管理的每日中间价机制管控人民币汇率，并维持严格资本管制。2023 年，央行曾指令银行下调美元存款利率，以抑制囤积美元行为并支撑走弱的人民币。当前人民币升值反映市场对美联储宽松货币政策的预期，汇率近月从 7.3 上方升至 7.1 左右。因国内贷款需求疲软且央行自 2023 年以来多次降息，中国银行净息差持续收窄。

**标签**: `#China economy`, `#yuan exchange rate`, `#banking policy`, `#currency management`, `#dollar deposits`

---

<a id="item-7"></a>
## [中国将对美贸易休战延长两个月](https://news.google.com/rss/articles/CBMisAFBVV95cUxOSTA2TElMOUVJb2VPUWp2RnhuNWtoOHhncWpKUW9Ob1lEQ19BVUluTWRvRkZTYWJTYlU5RlZNR2F6UmZOcW5GLXlrQVJuMzMxakd2V2M4d1dXRDBCU3FBN182RlFQTjVBbVpTbzQ2cXZzdkk4YUJxZkF4NUVoZXlXR1haVlZIY2lpMnJQeTdFWTFMQkR5QWxiaWtqZUJSSUI5bFpzdGNmUENfU2h4dWIxcg?oc=5) ⭐️ 8.0/10

中国同意将与美国的贸易休战延长两个月，继续暂停对美加征的 24%关税税率，同时维持对美实体不可靠实体清单与出口管制措施的暂停。美国财政部长 Scott Bessent（斯科特·贝森特）于周三宣布这一延长，将截止日期推至 11 月之后，并配合双方就更大协议进行的持续谈判。 这两个月的延长避免了世界前两大经济体之间的关税立即升级，为全球供应链和围绕 11 月截止日期规划的企业提供了稳定性。这表明双方尽管在结构性问题上仍有分歧，但仍致力于谈判，且时机与中国国家主席习近平可能出席在迈阿密举行的 G20（二十国集团）峰会相吻合。 中国商务部确认，对美加征 24%关税的暂停及不可靠实体清单措施的暂停将从原到期日起继续两个月。Scott Bessent（斯科特·贝森特）在福克斯新闻采访中表示，美中同意延长所谓的釜山协议——一种临时贸易休战，同时致力于达成更大协议。CSIS（战略与国际研究中心）学者 Scott Kennedy（斯科特·肯尼迪）指出，延长显示美国对中国提议仍不满意。

rss · Reuters \(English\) · 11月9日 10:48

**背景**: 贸易休战源于 APEC（亚太经合组织）会议期间达成的釜山协议，双方同意在就知识产权、强制技术转让和市场准入等结构性问题谈判期间暂停关税升级。此前几轮关税中，美国对超过 3600 亿美元中国商品加征关税，中国则对约 1100 亿美元美国产品进行反制。24%额外关税的暂停最早于 2024 年 5 月宣布，作为财政部长 Bessent（贝森特）和中国副总理何立峰牵头的高层谈判前的善意姿态。

**标签**: `#China-US relations`, `#trade policy`, `#tariffs`, `#international trade`, `#economy`

---

<a id="item-8"></a>
## [药明康德获美国国防部从 1260H（2021 财年国防授权法案第 1260H 条）中国军工企业名单移除](https://36kr.com/newsflashes/4063176754156417?f=rss) ⭐️ 8.0/10

2026 年 11 月 9 日，美国国防部（DoD）决定将药明康德（02359.HK）从 1260H（2021 财年国防授权法案第 1260H 条）中国军工企业（CMC）名单中移除，遵从联邦法院于 2026 年 8 月 7 日作出的初步禁令裁决。药明康德于 11 月 10 日通过港交所公告披露此事，称国防部副部长判定应遵从法院 7 月 22 日聆讯及后续裁决的命令。该决定使公司免受该认定带来的进一步不利商业与声誉影响。 此次移除标志着中国生物医药企业罕见地通过司法途径成功挑战五角大楼认定，该认定依据行政令 13959（第 13959 号行政令）触发投资禁令及美国政府承包商供应链限制。药明康德作为全球医药供应链关键节点，为辉瑞、默克、诺华等跨国药企提供研发外包服务，移除减少了客户端的合规不确定性。该案例亦为 2026 年 6 月同期被列入名单的阿里巴巴、百度、比亚迪等企业提供了司法救济先例。 法院于 2026 年 7 月 22 日就初步禁令动议举行聆讯，并于 8 月 7 日作出裁决批准动议，强制国防部从更新后的 CMC 名单中移除药明康德。公告引述公司承诺：「我们将继续致力于服务我们的客户，赋能其为病患研制拯救和改善生命之药物。」1260H 名单依据 2021 财年国防授权法案（NDAA）每年更新；药明康德于 2026 年 6 月更新时被列入，同期新增实体还包括数十家中国科技与制造企业。

rss · 36氪 · 11月10日 07:57

**背景**: 2021 财年威廉·M·（麦克）·索恩贝里国防授权法案（NDAA）第 1260H 条要求五角大楼每年发布其认定为在美国运营的「中国军工企业」名单。列入名单触发第 13959 号行政令（2020 年 11 月特朗普签署，拜登通过第 14032 号行政令扩展）下的投资禁令，禁止美国人士买卖相关实体证券。2026 年 6 月更新将药明康德、阿里巴巴、百度、比亚迪、TP-Link 等纳入，引发相关企业抗议并否认军方关联。药明康德随后在美国联邦法院提起诉讼，主张认定缺乏证据且属武断，最终获得初步禁令救济。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dentons.com/en/insights/alerts/2026/june/18/dod-expands-section-1260h-chinese-military-companies-list">DoD Expands Section 1260 H “ Chinese Military Companies ” List</a></li>
<li><a href="https://en.wikipedia.org/wiki/Executive_Order_13959">Executive Order 13959 - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/06/09/alibaba-baidu-byd-named-on-pentagons-china-military-list-.html">Alibaba, Baidu, BYD named on Pentagon&#x27;s China military list</a></li>

</ul>
</details>

**标签**: `#生物医药`, `#中美关系`, `#药明康德`, `#监管政策`, `#资本市场`

---

<a id="item-9"></a>
## [特朗普预计在华 APEC 峰会会晤习近平和普京](https://news.google.com/rss/articles/CBMiakFVX3lxTE5zakR1R2VMWnJzN0VHS0FMakQwbDNnRlJqOEdVR0FQSV9MR2o1N1ZWQml1TlZOTWFlYTJucG1rbDRTZjl2X1FWRzRvSzJvcGlGOS1VdXZHX2RHM3g3dkdFdGJzdkRlZlhtY1E?oc=5) ⭐️ 8.0/10

美国前总统特朗普于 11 月 8 日表示，预计将在深圳举行的 APEC（亚太经合组织）峰会期间，分别与中国国家主席习近平和俄罗斯总统普京举行双边会晤。特朗普形容即将到来的会面「将会很有意思」，据路透社报道引述。 美国、中国、俄罗斯三国领导人若在同一多边场合密集会晤极为罕见，可能预示着在贸易摩擦、乌克兰危机及印太安全等议题上的大国外交走向。会晤结果将直接影响中美关系、中俄协作及亚太地区的地缘政治平衡。 特朗普于 11 月 8 日当地时间向记者明确点名习近平和普京为预期会晤对象。中方此前披露，习近平曾告知特朗普，双方年内将会面两次：11 月在深圳 APEC（亚太经合组织）峰会、12 月在迈阿密 G20（二十国集团）峰会。APEC 峰会举办地已确认为中国深圳。

rss · 联合早报 · 11月9日 07:59

**背景**: APEC（亚太经合组织）是推动亚太自由贸易的 21 个成员论坛，2025 年峰会由中国在深圳主办。上一次三国领导人同框出席 APEC 领导人会议还是 2017 年；此后因乌克兰危机制裁，俄罗斯缺席或以视频形式参会。特朗普此番表态正值其竞选重返白宫期间，其外交预判具有高度政治敏感性。

**标签**: `#国际政治`, `#中美关系`, `#中俄关系`, `#APEC峰会`, `#特朗普`

---

<a id="item-10"></a>
## [太原豪生公寓火灾致 14 死 喷淋系统失灵](http://www.infzm.com/contents/344509) ⭐️ 8.0/10

2026 年 11 月 8 日 16 时 59 分，山西省太原市迎泽区柳巷南路豪生国际公寓配楼 4 层起火，火势蔓延至 8、9 层。截至 11 月 9 日新闻通气会通报，事故造成 14 人遇难、25 人受伤，产权单位管理人员及物业公司负责人已被采取控制措施。 这起火灾暴露出建筑消防系统的严重失效：幸存者称喷淋头不出水反冒烟、全程无火警无人员疏散。14 人死亡发生在核心商圈的混合用途高层建筑中，引发对老旧改建建筑消防规范执行力度及物业管理问责的紧迫追问。 幸存者兰田（32 岁）入住咕奈酒店 8 层西北角房间，称「房间的防火喷淋头没有喷水，反而向外冒出烟雾」，且全程无火警、无工作人员通知。他与 6 名陌生人躲入带露台客房等待约 45 分钟，靠消防云梯获救。该楼 2007 年建成、曾称「盘古一号」，2021 年 12 月 24 日曾因手电筒充电引发 26 层火灾。

rss · 南方周末 · 11月9日 23:55

**背景**: 豪生国际公寓建于 2007 年，位于太原柳巷商业核心区，紧邻钟楼街步行街（2025 年客流 2207 万人次）。主楼 41 层、配楼 9 层，现业态以酒店、教培机构为主。同楼勃尔泰酒店称每 2-3 月接受消防检查、烟感正常；邻近商铺主称每年定期消检、社区月检，均归同一物业公司管理。

**标签**: `#火灾`, `#太原`, `#公共安全`, `#建筑安全`, `#问责`

---

<a id="item-11"></a>
## [英飞凌（Infineon）实现全球首个 300 毫米碳化硅功率器件](https://www.infineon.com/press-release/2026/infpr202611-028) ⭐️ 7.0/10

2026 年 11 月 9 日，英飞凌（Infineon）宣布在奥地利林茨工厂成功制造出基于 300 毫米（12 英寸）碳化硅（SiC）晶圆的功能性功率器件，实现行业首创。该突破利用现有 300 毫米硅晶圆设备经改造后用于 SiC 工艺，为大规模量产奠定基础，单片晶圆可产出芯片数量是现行 200 毫米标准的 2.3 倍。 向 300 毫米 SiC 晶圆过渡对降低宽禁带功率半导体成本至关重要，这些器件是电动汽车逆变器、光伏逆变器和电网基础设施的核心。英飞凌利用成熟的 300 毫米硅晶圆厂设备，无需新建产线即可加速扩产，有望缓解限制电动汽车普及的 SiC 供应短缺。这使英飞凌在商业化大批量 300 毫米 SiC 制造竞赛中领先于 Wolfspeed 等竞争对手。 英飞凌新闻稿强调，300 毫米工艺可行性是通过改造现有设备而非定制工具实现的，大幅降低了资本支出。公司未披露量产爬坡的具体时间表，但功能器件的演示表明工艺开发已进入先进阶段。社区评论指出 Wolfspeed 可能在 2026 年初已具备 300 毫米能力，但英飞凌声称在该晶圆尺寸上实现了行业首个功能性功率器件。

hackernews · sshah03 · 11月10日 02:25 · [社区讨论](https://news.ycombinator.com/item?id=50429430)

**背景**: 碳化硅（SiC）是一种宽禁带半导体，禁带宽度约 3.2 电子伏特（eV），使器件能在比硅更高的电压、温度和开关频率下工作。功率电子行业多年使用 150 毫米和 200 毫米 SiC 晶圆，但晶体生长缺陷和晶锭尺寸限制推迟了 300 毫米过渡（硅在 2000 年代初已完成）。总部位于德国诺伊比贝格的英飞凌是全球营收最大的功率半导体厂商，在马来西亚古林建设新晶圆厂等大力投资 SiC。SiC 和氮化镓（GaN）等宽禁带材料被视为通过更高效功率转换实现全球脱碳目标的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techpowerup.com/354619/infineon-starts-worlds-first-300-millimeter-power-silicon-carbide-sic-wafer-production">Infineon Starts World&#x27;s First 300-Millimeter Power Silicon Carbide ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wide-bandgap_semiconductor">Wide - bandgap semiconductor - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Silicon_carbide">Silicon carbide - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者质疑为何 300 毫米过渡耗时如此之久，因为 300 毫米硅设备已存在数十年，有人指出 Wolfspeed 可能已具备 300 毫米能力。也有人惊讶英飞凌未追求大语言模型（LLM）加速器芯片，尽管林茨附近有 AI 研究机构。另一讨论呼吁欧洲重启动态随机存取存储器（DRAM）生产，反映出对半导体主权的更广泛战略担忧。

**标签**: `#semiconductors`, `#silicon-carbide`, `#power-electronics`, `#manufacturing`, `#Infineon`

---

<a id="item-12"></a>
## [Fervo Energy 获得 120 亿美元增强型地热系统订单](https://techcrunch.com/2026/11/09/fervo-now-has-12b-in-orders-for-its-geothermal-power-tech/) ⭐️ 7.0/10

Fervo Energy 在第三季度财报中披露已签约收入达 119 亿美元，较上季度的 72 亿美元大幅增长，这得益于 Google 等超大规模数据中心运营商对其增强型地热系统（EGS，Enhanced Geothermal Systems）的强劲需求。该公司位于犹他州的 Cape Station 项目资源量达 8.4 吉瓦，计划于 2028 年底前为 Google 完成 396 兆瓦电厂，且已于今年早些时候将首座 100 兆瓦电厂并网发电。 120 亿美元的订单簿标志着增强型地热系统（EGS）实现商业化可行性，能为 AI 数据中心提供全天候无碳基荷电力。若 Fervo 达成 3000 美元/千瓦的长期成本目标，其发电成本将低于当前天然气价格，可能重塑清洁能源转型中基荷电源的竞争格局。 Fervo 单位千瓦成本已从 Cape Station 一期的 7000 美元降至 Google 项目的 5500 美元，含补贴后相当于天然气价格 6 美元/百万英热单位（MMBtu）。CEO Tim Latimer 表示：「我们按计划建设 Cape Station，Google 可按自家进度开发数据中心，双方互不等待。」公司持有 19 亿美元现金、长期债务 3.016 亿美元，但本季录得 4370 万美元经营亏损。

rss · TechCrunch · 11月10日 04:55

**背景**: 增强型地热系统（EGS）借用石油天然气行业的水平钻井和水力压裂技术，在干热岩层中人工构建储热层，突破传统地热仅限天然热水资源的局限。美国能源部（DOE，Department of Energy）预测 EGS 到 2050 年可提供 90 吉瓦以上清洁电力。Fervo 成立于 2017 年，率先将页岩气钻井技术应用于地热开发，并于 2021 年与 Google 签署内华达州试点项目电力购买协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Enhanced_geothermal_system">Enhanced geothermal system - Wikipedia</a></li>
<li><a href="https://www.energy.gov/hgeo/geothermal/enhanced-geothermal-systems">Enhanced Geothermal Systems | Department of Energy</a></li>

</ul>
</details>

**标签**: `#geothermal energy`, `#clean energy`, `#energy technology`, `#Fervo Energy`, `#energy transition`

---

<a id="item-13"></a>
## [美国国防部长赫格塞斯本周面临众议院弹劾投票](https://news.google.com/rss/articles/CBMipgFBVV95cUxOMWxSRW95b2hyeC00X2Q5VmF0alVielFMcVhtMVFhdFBfRUNmQlAyM3IwUkthb3JDYldrNmhuX1dVXzRRS21LMWNxX2Q2VHN3WGdOSHRyVkVBSVc1UHpIYmVFYjRvUFlIS292a3VPMkljcW5HWVBYVkdpX1ZKSE1qRWs2T21JRm9pcjZVMzRSR0FVZk1fMUs5QlhCTnBFVXpUczJIbW1n?oc=5) ⭐️ 7.0/10

美国国防部长皮特・赫格塞斯预计本周将面临众议院弹劾投票，肯塔基州共和党众议员托马斯・马西于周一提出了弹劾决议。路透社 11 月 9 日报道称，赫格塞斯淡化弹劾风险，表示已准备好在五角大楼为自己的履历辩护。这将是国会罕见地试图罢免一位在任国防部长。 对在任国防部长的弹劾投票极为罕见，可能在涉及伊朗等潜在冲突的持续军事行动中动摇五角大楼领导层。此举反映共和党内部深层分裂，马西作为共和党人批评特朗普任命的官员。结果可能影响美国军事政策、指挥链及国际盟友对美国国防领导层的信心。 众议员托马斯・马西（肯塔基州共和党）周一提出弹劾决议，指控赫格塞斯未经国会批准发动战争。赫格塞斯在周四视频声明中誓言对抗弹劾，并为伊朗战争辩护称其&quot;勇敢且具有历史意义&quot;。众议院预计本周投票，但参议院需三分之二多数才能定罪并将其免职。

rss · Reuters \(English\) · 11月10日 06:54

**背景**: 皮特・赫格塞斯曾任福克斯新闻主持人、陆军国民警卫队老兵，2025 年经参议院激烈听证后获确认为国防部长。美国宪法允许因&quot;重罪和轻罪&quot;弹劾文职官员，但历史上仅三名内阁官员被弹劾，均未被成功免职。上一位面临严重去职压力的国防部长是詹姆斯・马蒂斯，他在 2018 年选择辞职而非面对国会行动。

**标签**: `#US politics`, `#impeachment`, `#Pentagon`, `#US-China relations`, `#defense`

---

<a id="item-14"></a>
## [波音因生产困境裁减商用飞机部门 5%员工](https://news.google.com/rss/articles/CBMiyAFBVV95cUxOYVdQLTVQc2wtZzFUaDBNM3phQnpkZ0dfUlBXY2N3Z1BYcnZ3ajlMVjByY0gtcXExaWx5Qmx6T2M5LS1TMVhKb21teGtmZ082TmdoRGhGZkQwMTlqQzhncDFZaDhhNW9Rbml4VVZRSTZlTGRGb29JYW1pVUsxNUt4amNpdTlVTmRxZmdTMk0zNW55UXRLSHE5a0ZpZDFJenQwd2hPWjZ0UFZ2NzhiYl9meWphV0YzR1REZWNSOGRuMDZHTl9qdE1odw?oc=5) ⭐️ 7.0/10

波音商用飞机部门负责人斯蒂芬妮·波普在周一的内部备忘录中宣布，计划裁减该部门 5%的员工，约 2,525 人（基于 50,494 人的总编制）。裁员将通过自然减员和非自愿裁员方式进行，最早于 12 月发出通知，美国多州要求提前 60 天通知。 这是自 CEO 凯利·奥特伯格 2024 年 8 月上任后宣布裁减 17,000 个职位以来的首次人员削减，显示波音的转型仍远未完成。削减产量将冲击全球航空供应链，并可能影响中国等主要航空市场的交付节奏。 波普在备忘录中表示：「正如我们在第三季度财报中所述，我们需要重新调整产能提升的节奏，以便为我们的工厂和供应链合作伙伴争取更多时间，实现运营稳定。」商用飞机部门现有员工 50,494 人，5%裁减约 2,525 人；此次裁员为奥特伯格 2024 年 10 月宣布大规模裁员后的首次后续行动。

rss · Reuters \(English\) · 11月10日 06:33

**背景**: 波音长期面临 737 MAX 和 787 梦想客机的生产质量问题，FAA（美国联邦航空管理局）曾限制 737 MAX 月产量不超过 38 架。供应链瓶颈、监管审查及交付延迟迫使公司多次下调产能目标。奥特伯格 2024 年 8 月接任 CEO 后，推行「安全第一」战略并启动大规模裁员以精简运营。

**标签**: `#Boeing`, `#Aviation`, `#Workforce`, `#Manufacturing`, `#Global Economy`

---

<a id="item-15"></a>
## [沙特东西向输油管线在麦地那地区遭袭](https://news.google.com/rss/articles/CBMiugFBVV95cUxQeEtKMGZOdkpGT0I4d1dsaUtDQjlLSlhyV1o4M0Rqcm5KZHV4ZHhXeEdnTUwwV0x5eU1Ldmo1cFk0RG16SnFCMlZ0SkNlQzBmdkxPU2pmdmNqWmYwNEcwWGVVeEVNQVhqTnduTnZYNnVqZ3padlFRRkpGNGpYWHRRYVJsX0h3SXN6OFVaTWI2TGFfUVV2LVpLUGtydXppb0VFaDBNZy1YZ2pXWS1XSUxOTng3ZVpkZ18xd1E?oc=5) ⭐️ 7.0/10

11 月 9 日星期一，沙特阿拉伯东西向原油管线在麦地那地区遭到袭击，沙特通社援引能源部官员消息证实。袭击引发有限火灾，火势已被扑灭，未造成人员伤亡，管线运营未受影响。路透社和沙法克新闻均依据官方声明报道了此事。 东西向管线是沙特绕过霍尔木兹海峡的主要替代出口通道，设计输送能力约为日均 500 万桶。该基础设施若受干扰，将收紧全球原油供应并加剧价格波动，直接影响依赖海湾石油超 40%的中国等主要进口国。此次袭击凸显地区紧张局势下海湾能源设施持续面临的安全风险。 沙特通社引述能源部官员表示，管线「周一在该国西部麦地那地区遭到袭击，引发『有限火灾』，火势已扑灭」。目前无组织认领责任，沙特当局未披露袭击手段，但此前类似事件多涉及无人机或导弹。这条全长约 1200 公里的管线连接东部油田与红海亚努卜港。

rss · Reuters \(English\) · 11月10日 01:43

**背景**: 东西向管线（Petroline）于 1985 年投运，后扩建至日均 500 万桶产能，为沙特提供战略灵活性，以便在霍尔木兹海峡受阻时仍能出口原油。2019 年，胡塞武装无人机曾袭击该管线泵站，导致输送一度中断。2026 年维基百科条目预设伊拉克境内发射无人机袭击该管线的场景，凸显其被视为脆弱目标。沙特仍是全球最大原油出口国，日均出口约 700 万桶。

**标签**: `#Saudi Arabia`, `#oil pipeline`, `#energy security`, `#Middle East`, `#oil markets`

---

<a id="item-16"></a>
## [FDA（美国食品药品监督管理局）强制要求 Ozempic 和 Zepbound 增加眼部风险警示](https://news.google.com/rss/articles/CBMiwgFBVV95cUxQUG9HX0xJekVOS0FKR3BLMDJBSVJ6SEFrd2FSTU1aUmp1bTR0Vzl6V2Ewand4MTNVbGlTSXhFZEtGM19WZzhieEZrN3paaW1PWUVkZHlWdy1YalQ1OFlWblV4REdtc1hMQzlzTWJmWFRVRmNnNDdVY05oS292b00yTHQtZnh5djFrbTBpdGJDUnJ3akQ0ZlZoRzhaUXRDMXRURFhuM3lySkg4bnBmeDQyN0NjYXJIMDJJRW1LSUhxNHR0Zw?oc=5) ⭐️ 7.0/10

美国 FDA（食品药品监督管理局）于周一责令诺和诺德和礼来公司在 Ozempic（司美格鲁肽）和 Zepbound（替尔泊肽）的处方标签上新增非动脉性前部缺血性视神经病变（NAION）警示。该机构指出，上市后报告和观察性研究发现了一种罕见但严重的突发性视力丧失风险，可能导致永久性失明。这两款药物均为 GLP-1 受体激动剂，广泛用于 2 型糖尿病治疗，并在更高剂量下用于慢性体重管理。 该警示影响全球数百万使用这两款重磅药物治疗糖尿病或肥胖的患者，中国已批准上市且处方量大。NAION 被称为「眼卒中」，一旦视力受损目前无有效治疗手段，因此早期识别和知情同意至关重要。此举也标志着 FDA 对快速扩张的 GLP-1 类药物（现已涵盖多项心血管和代谢适应症）加强监管审查。 FDA 引用 2024 年《JAMA Network Open》队列研究，显示使用司美格鲁肽或替尔泊肽患者的 NAION 发病率比使用其他降糖药患者高约两倍，但绝对风险仍低，约为每 1 万患者年 1-2 例。诺和诺德和礼来须在 30 天内提交更新标签；FDA 同时敦促医护人员在治疗前后与患者讨论突发视力变化等症状。

rss · Reuters \(English\) · 11月10日 01:35

**背景**: GLP-1 受体激动剂如司美格鲁肽（Ozempic、Wegovy）和替尔泊肽（Mounjaro、Zepbound）已成为全球增长最快的药物类别，2024 年合计销售额超 500 亿美元。NAION 由视神经乳头供血不足引起，导致单眼突发无痛性视力丧失，一般人群年发病率约为十万分之 2-10。此前标签仅列出常见胃肠道副作用，未强调视神经缺血风险。FDA 此举紧随 2024 年欧洲药品管理局（EMA）审查，后者同样建议更新产品信息以反映该风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Non-arteritic_anterior_ischemic_optic_neuropathy">Non-arteritic anterior ischemic optic neuropathy</a></li>
<li><a href="https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2837377">Semaglutide or Tirzepatide and Optic Nerve and Visual Pathway ...</a></li>
<li><a href="https://www.ajmc.com/view/semaglutide-tirzepatide-linked-to-small-increase-in-eye-disorder-risk">Semaglutide, Tirzepatide Linked to Small Increase in Eye ...</a></li>

</ul>
</details>

**标签**: `#FDA`, `#drug safety`, `#Ozempic`, `#Zepbound`, `#health`

---

<a id="item-17"></a>
## [泽连斯基在俄乌谈判前与莫迪通话](https://news.google.com/rss/articles/CBMinAFBVV95cUxNbWZZUjlKNXFxRjZNbUZGcVFVdUFEZzJBY1pJZ2JVYVJHd3FuWkVrMllmcnhZU1NKbEVJdDNfbkI3MXhsOTh1V3ItQlZocXcyOWZNN0hsX1hiRWRDVzRGUEhRS20zX1RDNmlJalM5dGNJZ2ZtM194QnZPOWNPVXVSQ3ZrUVRkZGpzYzFYRnFoNmlSdXZ4WjNiNm96MGU?oc=5) ⭐️ 7.0/10

乌克兰总统泽连斯基在预期的俄乌和谈前与印度总理莫迪通话。通话发生在莫迪与俄罗斯总统普京进行 50 分钟通话之前，普京在通话中向莫迪通报了谈判进展。莫迪曾多次与两国领导人接触，包括去年 5 月在日本广岛 G7（七国集团）峰会期间会见泽连斯基。 印度的外交介入使其成为俄乌冲突的潜在调解人，利用其与莫斯科和基辅的双边关系。莫迪在和谈前与双方领导人接触可能影响谈判动态，体现印度日益增长的全球外交角色。作为全球南方大国，印度的参与为此前由西方和俄罗斯主导的和平努力增添了新维度。 莫迪在与普京进行 50 分钟通话前先与泽连斯基通话，普京在通话中向莫迪通报谈判进展。莫迪曾多次与两国领导人交谈，并于 2024 年 5 月在日本广岛 G7（七国集团）峰会会见泽连斯基。这些通话发生在预期的俄乌和谈前，但和谈具体日期尚未公布。

rss · Reuters \(English\) · 11月9日 22:38

**背景**: 自 2022 年 2 月俄罗斯全面入侵乌克兰以来，印度保持中立立场，继续购买俄罗斯石油同时主张对话外交。莫迪总理将印度定位为全球南方的声音，在整个战争期间与乌克兰和俄罗斯领导人保持接触。2023 年 5 月日本广岛 G7（七国集团）峰会为莫迪和泽连斯基提供了首次面对面会晤平台，双方讨论了乌克兰和平公式。自 2023 年以来，印度的潜在调解角色备受关注，莫斯科和基辅均承认新德里的独特地位。

**标签**: `#Ukraine-Russia conflict`, `#diplomacy`, `#India`, `#Zelenskiy`, `#Modi`

---

<a id="item-18"></a>
## [礼来口服减重药 Foundayo（福达ヨ）后期试验显著改善睡眠呼吸暂停](https://news.google.com/rss/articles/CBMi1wFBVV95cUxORmpPM1Z4S081Y1hSZFBJMGFSeTdBY3RMZmhiNUZNTnNkckN4ZUNXUDFmYi01NktZaVRWVC1kTWZaaDFXWjRZNXljX2h4eTJpeTZuNkpPczRQOHptNlRtZG1iUWxjZmhqZ3VrVjhYUjFyN1pTWWxEZWx6ZXNHVkowSV8xdlhzb1A0N09UT1lPZ3ZpWUwtWl84VUZoV3pvZlh0OWZraFFfZFZXWEJfNWZITGpzU00yYzFRZWt6T21aXzJMZ0RfTk8zSTB5U0NTcGp5b3Vzb2o0MA?oc=5) ⭐️ 7.0/10

礼来公司于周一（11 月 9 日）宣布，其口服 GLP-1（胰高血糖素样肽-1）受体激动剂 Foundayo（福达ヨ，通用名 orforglipron 奥弗格鲁肽）在后期临床试验中达到主要终点，显著减少了中重度阻塞性睡眠呼吸暂停（OSA）肥胖成年患者的睡眠呼吸暂停发作次数。药企计划在 2026 年底前向美国 FDA（食品药品监督管理局）提交该适应症的上市申请，该药已于 2026 年 4 月获批用于减重。消息公布后，礼来股价上涨逾 3%。 这一结果使 Foundayo（福达ヨ）成为首个拥有 III 期数据支持治疗睡眠呼吸暂停的口服 GLP-1（胰高血糖素样肽-1）疗法，有望突破目前仅有注射剂 Zepbound（替尔泊肽，于 2024 年 12 月获 FDA 批准用于 OSA）的局面。每日一片的口服制剂可提升依从性——据估计约 80% 的 OSA 患者合并肥胖，且许多人难以坚持 CPAP（持续正压通气）治疗，美国 alone 就有逾 3000 万 OSA 患者。口服制剂还免除了冷链运输，降低了包括中国在内全球市场的准入门槛，而中国肥胖与 OSA 患病率正快速上升。 试验显示呼吸暂停低通气指数（AHI，阻塞性睡眠呼吸暂停严重程度的标准指标）具有统计学显著性下降，但初步公告未披露具体数值。Foundayo（福达ヨ）为每日一次 12 毫克奥弗格鲁肽片剂，可随餐或空腹服用，区别于部分需空腹注射的 GLP-1（胰高血糖素样肽-1）药物。礼来计划在 2026 年底前提交上市申请，若获批最早可于 2027 年在美国上市。其作用机制为激活 GLP-1 受体抑制食欲并减轻体重，从而缓解导致 OSA 的上气道解剖性阻塞。

rss · Reuters \(English\) · 11月10日 00:57

**背景**: 阻塞性睡眠呼吸暂停（OSA）在全球影响约 9.36 亿成年人，其中 60%-90% 合并肥胖，使减重成为核心治疗策略。长期以来治疗依赖 CPAP（持续正压通气）机器，但依从率不足 50%，而减重手术存在手术风险。礼来的注射剂替尔泊肽（商品名 Zepbound/Mounjaro）于 2024 年 12 月成为首个获批治疗 OSA 的药物，其 SURMOUNT-OSA 试验显示 AHI 最高降幅达 63%。Foundayo（福达ヨ，奥弗格鲁肽）是礼来第二代口服 GLP-1（胰高血糖素样肽-1）候选药，机制上不同于替尔泊肽的双重 GIP/GLP-1 作用，2024 年进入 III 期开发，此前 II 期数据显示 36 周体重最多减轻 14.7%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/220934Orig1s000lbl.pdf">FOUNDAYO</a></li>
<li><a href="https://www.drugs.com/drug-class/glp-1-receptor-agonists.html">GLP - 1 Drugs ( GLP - 1 Agonist ) - List of Brands &amp; Generics</a></li>
<li><a href="https://www.thelondongeneralpractice.com/obstructive-sleep-apnoea-and-weight-loss-treating-the-underlying-cause/">Obstructive Sleep Apnoea and Weight Loss, Treating the Underlying...</a></li>

</ul>
</details>

**标签**: `#医药研发`, `#减重药物`, `#睡眠呼吸暂停`, `#临床试验`, `#礼来公司`

---

<a id="item-19"></a>
## [欧盟（European Union）外交负责人卡拉斯指责俄罗斯假装谈判实则轰炸平民](https://news.google.com/rss/articles/CBMinwFBVV95cUxOV2JEbVRTVVAxUDdfY2lCZ3JheVZ5QXdOck1vSDR3X2NpR1dCV1NxcnJITm1xN0Y1VFZ4ZlpibWcxNlJZeXg1YmYycW1GbkQ3RWo3Ym5MZDAzempjaWhRLXFNOEp5ZVBEeS1EMFI1NzF6LVM0UDRiSkdocFBMeWZlRnFXaE01XzRqVWxnS1djYk1lUW5rbDZ3eHhCNUZlYTA?oc=5) ⭐️ 7.0/10

欧盟（European Union）外交与安全政策高级代表卡娅·卡拉斯（Kaja Kallas）指责俄罗斯在乌克兰问题上假装谈判，同时持续轰炸平民，并指出莫斯科未派遣有决策权的官员参加会谈。她在周三的欧盟外长会议上发表上述言论，会议讨论结束俄乌战争的努力。卡拉斯强调，关注点应放在俄罗斯方面的让步上，而非施压乌克兰。 卡拉斯的指控显示欧盟（European Union）立场强硬，认为俄罗斯缺乏诚意谈判，这可能推动更严厉制裁或增加对乌军事援助。该言论反映欧盟领导人在战争持续两年多仍无可信和平路径下的挫败感。这也凸显了外交僵局，使涉及大国的未来停火谈判更加复杂。 卡拉斯表示：「俄罗斯只是假装谈判」，「他们没有派遣有决策权的人参加这些会谈」。她主张欧盟（European Union）「不应乞求俄罗斯」谈判，而应迫使俄罗斯进行真诚谈判。周三的欧盟外长会议聚焦俄罗斯可能提供何种让步以结束战争。

rss · Reuters \(English\) · 11月10日 00:12

**背景**: 卡娅·卡拉斯于 2024 年 12 月出任欧盟（European Union）外交与安全政策高级代表，此前曾于 2021 至 2024 年担任爱沙尼亚总理。俄乌战争始于 2022 年 2 月 24 日俄罗斯全面入侵，已造成数十万人伤亡。此前包括 2022 年 3 月伊斯坦布尔会谈在内的多轮和平倡议均未达成持久协议。欧盟自 2022 年以来已实施 14 轮对俄制裁，并向乌克兰提供超过 1000 亿欧元的财政、人道及军事援助。

**标签**: `#Russia-Ukraine war`, `#EU diplomacy`, `#Kaja Kallas`, `#geopolitics`, `#international relations`

---

<a id="item-20"></a>
## [比亚迪仰望在阿布扎比全球首发鼎曜超豪华轿车 预估售价 200 万元](https://36kr.com/p/4062540807099270?f=rss) ⭐️ 7.0/10

2026 年 11 月 7 日，比亚迪旗下高端品牌仰望在阿联酋阿布扎比全球首发超豪华行政旗舰轿车鼎曜，提供行政版与山河鼎韵限量版两个版本，预估售价约 200 万元人民币，计划于 2027 年第二季度交付。这是仰望首次以完整品牌形象在海外举办全球发布会，直接将竞争对手锁定为劳斯莱斯、宾利等传统超豪华品牌。 此次发布标志着比亚迪从追求出口规模转向高端品牌引领，其新能源乘用车出口量已从 2022 年的 5.59 万辆跃升至 2025 年的 104.96 万辆，2026 年前十月更达 150.74 万辆。鼎曜能否进入全球超豪华消费者的选择名单，将检验中国品牌能否凭借东方文化叙事与易四方四电机平台、璇玑 A3 智驾芯片等自研技术，打破欧洲传统品牌在超豪华细分市场的长期垄断。 鼎曜车身尺寸为 5600×2030×1590 毫米、轴距 3500 毫米，采用礼宾级中轴对开门，设计灵感源自中国传统礼器&\#x27;鼎&\#x27;并融入甲骨文车标。核心技术包括易四方四电机独立驱动系统（支持高速爆胎稳行与应急浮水）、云辇全主动车身控制系统（具备路面预瞄）、比亚迪自研璇玑 A3 智驾芯片、第二代刀片电池及闪充技术，CLTC（中国轻型汽车行驶工况）工况续航超 1000 公里。山河鼎韵限量版还融入苏绣与和田玉工艺；数据显示 2026 年前三季度比亚迪在阿联酋销量达 11495 辆。

rss · 36氪 · 11月9日 21:10

**背景**: 比亚迪新能源乘用车出口量从 2022 年的 5.59 万辆激增至 2026 年 1—10 月的 150.74 万辆，已成为中国最大汽车出口企业。过去其出海竞争力主要依赖新能源技术、供应链效率与性价比，但建立高端品牌认知成为新课题。中东尤其是阿联酋拥有成熟的超豪华车消费市场，是劳斯莱斯、宾利等欧洲传统品牌的核心竞技场。易四方平台于 2023 年 1 月发布，是全球首个量产四电机独立驱动系统；云辇系统历时 5 年、耗资数十亿元全栈自研。中国采用的 CLTC（中国轻型汽车行驶工况）续航工况通常比美国 EPA（美国环保局）、欧洲 WLTP（全球统一轻型车测试程序）标准更宽松，公布里程偏乐观。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zsc.github.io/byd_history/chapter13.html">第十三章：易四方技术深度解析 | byd_history</a></li>
<li><a href="https://post.smzdm.com/p/aeqmq2e3/">post.smzdm.com/p/aeqmq2e3</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/695739382">浅谈电动汽车续航里程测试方法(EPA/WLTP/NEDC/CLTC)</a></li>

</ul>
</details>

**标签**: `#汽车产业`, `#新能源汽车`, `#比亚迪`, `#仰望`, `#高端制造`, `#全球化`

---

<a id="item-21"></a>
## [特朗普政府推动永续期货进入美国市场，华尔街老牌机构敲响风险警钟](https://news.google.com/rss/articles/CBMixwFBVV95cUxNYVZsYWtjTnU4dVhYU3o4LWJCeVdPOUNhNGdUVUhLdG1iZTE3REw3QmR6RHRzblFjc3RKYmlvS1JkRlFJakFpMExqdGx2ZDU1OGcxME5OazNFVTVGYTRQLTlSTjFhTk5Wc041TnV5dUtRdGdWWVQwWXRhMzdMaE9sdmdWOFROSGVoOTR1Z201THNOb25PTmdzWkdraGNkWEg2bFljcld6SDM0MzJvdG84amJkNGRBYjJyMDRCemVFMVhUMzZvcTZR?oc=5) ⭐️ 7.0/10

11 月 9 日，路透社报道特朗普政府正推动将离岸永续期货合约（perps，永续期货）引入美国市场，四位华尔街老牌机构高管因此发出风险警告。商品期货交易委员会（CFTC）委员 Caroline Pham 和 Summer Mersinger 暗示，在更宽松的监管路径下，加密货币永续期货可能「很快」上线，这标志着与前政府对加密衍生品审慎立场的重大背离。 永续期货让交易者无需持有标的资产即可无限期投机加密货币价格，通过资金费率将合约价格锚定现货市场；2025 年中心化交易所永续期货交易量达 86.2 万亿美元，同比增长 47%。将此类产品引入美国境内可能重塑衍生品市场结构，让散户投资者接触高杠杆的离岸式交易，并加剧芝加哥商品交易所集团（CME Group）等传统交易所与币安、Bybit 等原生加密平台的竞争。监管层担忧市场操纵、连环强平以及现有风控对 7×24 小时市场的适用性。 路透社采访的四位老牌机构高管警告，CFTC 加速的时间表绕过了标准的规则制定和压力测试流程。委员 Mersinger 在 11 月 6 日的行业活动上表示「加密货币永续期货很快就会推出」，但 CFTC 尚未发布这些合约的最终保证金或持仓限额规则。离岸平台目前对比特币永续期货提供高达 100 倍杠杆，远超美国受监管期货典型的 10–20 倍。政府的推动与其更广泛的亲加密议程一致，包括提议建立战略比特币储备。

rss · Reuters \(English\) · 11月10日 01:23

**背景**: 永续期货由 BitMEX 于 2016 年首创，后经币安、Bybit、OKX 推广成为主流加密衍生品工具，特点是无到期日并采用资金费率机制。在主席 Rostin Behnam 领导下，CFTC 曾对向美国人提供永续期货的离岸平台采取执法行动，包括 2021 年与 BitMEX 达成 1 亿美元和解。特朗普政府 2024 年竞选承诺「亲加密」监管改革，当选总统提名被视为业界友好的前 SEC 委员 Paul Atkins 出任 SEC 主席。华尔街老牌机构如 CME Group 虽已推出加密期货，但实施更严格的保证金和持仓限额。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/what-are-perpetual-futures-7494870">Understanding Perpetual Futures: A Guide for Cryptocurrency ...</a></li>
<li><a href="https://financefeeds.com/what-does-perp-mean-in-crypto-perpetual-futures/">What Does Perp Mean in Crypto? Futures That Never Expire</a></li>

</ul>
</details>

**标签**: `#Finance`, `#Regulation`, `#Trump Administration`, `#Derivatives`, `#Crypto`

---

<a id="item-22"></a>
## [中国将稀土出口管制暂停期延长至 1 月](https://news.google.com/rss/articles/CBMirwFBVV95cUxOMVo4bzYyXzJlM0RUaEJCaDNDQWZ2bzhKOFNmbzBNTnMzNW9UeGRqVm9vd0pDWkNZUnROTXVSRmZ4aFJ1ZW1SeFdfQXJhZmFOREt6R3JQa2NFb3dsa21BYkdRanpFLTdVT1JEUko5NnhTY2lTbVk4cTZZS2NvS3lSMWQ4YnpQbElVcElZMDlQNjE2cDg2VnVwZ3MySXRraGpZQUtJWndKemxDRTVlMzBF?oc=5) ⭐️ 7.0/10

中国商务部于 11 月 9 日周一宣布，将针对钬、铒、铥、铕、镱等五种稀土元素及相关加工技术、设备的出口管制豁免期延长两个月，原定本月到期的豁免现将持续至 1 月 10 日，保留了习特会后达成的广泛协议部分内容。 此举维持了全球半导体、电动汽车和国防体系所需关键矿产供应链的稳定，为进口国争取更多时间实现供应来源多元化；同时显示北京倾向以渐进措施而非突发限制管控贸易摩擦，直接影响依赖中国稀土加工的美国、欧盟、日本和韩国产业。 暂停范围涵盖钬、铒、铥、铕、镱五种重稀土元素及特定冶炼、分离、加工技术；中国于 2025 年 4 月首次对七种稀土实施管制，10 月扩大至 12 种，此次延期实为升级管制中的部分缓冲；豁免延长源于习特会共识，但报道未披露峰会具体日期。

rss · Reuters \(English\) · 11月9日 17:14

**背景**: 中国占全球稀土开采产量逾 60%、精炼产能近 90%，出口政策成为战略杠杆；2025 年 4 月以国家安全为由对钐、钆、镝等七种稀土实施管制，10 月扩大至 12 种并覆盖加工技术，推动美欧日韩加速本土开采与回收项目；习特会达成临时豁免安排，在谈判继续期间避免即时供应冲击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2025/10/27/business/china-rare-earth-export-controls.html">Step by Step, How China Seized Control of Critical Minerals - The...</a></li>
<li><a href="https://www.usgs.gov/programs/mineral-resources-program/science/what-are-critical-minerals-0">What are Critical Minerals ? | U.S. Geological Survey</a></li>

</ul>
</details>

**标签**: `#rare earths`, `#China policy`, `#critical minerals`, `#trade`, `#geopolitics`

---

<a id="item-23"></a>
## [南非选民在地方选举中拒绝 ANC（非洲人国民大会）多数席位](https://news.google.com/rss/articles/CBMiugFBVV95cUxNY0RIU1gtMURBQXJvZkZSTnI4MXVuYUdfdU9HNVRlUzMwZzE1TG9tY19LRnRNTjRYb2cyN0FqU2ZodTNrVTk5TW1zcER6WTQ1WFZ3SjdKWlhkYW5ZZExGaTUwU2IxcUFQSWt5dXhDTFNzaFRJaThHeEthYTZOS2RUUEhVb21ralBsa3poUHZTSlRSdFQ2ci1UeXAwcVR2VDJ3bzZocFJZWDVGTEszUFp2VTRuNU9IQVBLM0E?oc=5) ⭐️ 7.0/10

2024 年 11 月初的市政选举中，南非执政党 ANC（非洲人国民大会）自 1994 年以来首次失去绝对多数，全国得票率仅约 40%。11 月 9 日公布的结果迫使 ANC（非洲人国民大会）与民主联盟（DA）和经济自由战士党（EFF）等反对党展开联合组阁谈判。分析人士认为，这标志着选民因服务交付失败和腐败问题而惩罚执政党，而非延续对解放运动的忠诚。 ANC（非洲人国民大会）在约翰内斯堡和比勒陀利亚等经济中心失去多数控制权，标志着非洲最工业化经济体历史性地转向联合执政。作为 BRICS（金砖国家）创始成员和中国在非洲最大贸易伙伴，南非的政治碎片化可能影响外资政策连续性、矿业监管及其在全球治理议题上与北京的立场一致性。此结果也增强了反对党在 2026 年全国大选前的声势，或将重塑该国民主进程。 ANC（非洲人国民大会）全国得票率约 40%，较 2016 年市政选举的 54%大幅下滑；民主联盟（DA）得票约 22%，经济自由战士党（EFF）约 10%。联合组阁谈判预料艰难，DA（民主联盟）排除与 EFF（经济自由战士党）结盟，而 ANC（非洲人国民大会）内部对潜在合作伙伴存在分歧。总统西里尔·拉马福萨承认选民发出「明确信息」，承诺打击腐败并改善服务交付。独立选举委员会（IEC）确认投票率为 45.8%，为 1994 年以来最低。

rss · Reuters \(English\) · 11月10日 05:20

**背景**: ANC（非洲人国民大会）自 1994 年结束种族隔离的首次民主选举以来连续执政，在历次全国和大多数市政选举中均以舒适多数获胜。然而，经济增长放缓、失业率持续超 30%、电力短缺（限电）以及前总统祖马涉及的高调腐败丑闻，严重削弱了其支持基础。南非 2010 年加入 BRICS（金砖国家），与中国关系深化，中国成为其最大双边贸易伙伴，年贸易额超 500 亿美元。2024 年市政选举被视为 2026 年全国大选的风向标，ANC（非洲人国民大会）面临首次失去国家议会多数席位的风险。

**标签**: `#South Africa`, `#ANC`, `#election`, `#BRICS`, `#China-Africa relations`

---

<a id="item-24"></a>
## [阿联酋加尔加什警告地区长期不确定性，称美伊和解前景艰难](https://news.google.com/rss/articles/CBMixgFBVV95cUxQMlI2UXNzNl84Z1ByMV9Ybm5YNjMtZkdPcDhsZ2plZk9udWViZDZ4eTRVQVNXN2x6U2hENlkxbXJ2SXVvVU0tVWFkZGlSLXBDcnBZM1pzLVBNMzA5bjdZOHlFSXd6ZzhsWWZvV3JWWXlTME1tMnJ5Q0RoWHk1ZmJzbzk5cjZFaDI4NXpTOGRaVDBTNGNxcnRZYjF0X2NzY3EwaEJZcVhMaHRRMXREdXBkeXh6OGRCdU9aaWRJdS1zNzBQSUJCZEE?oc=5) ⭐️ 7.0/10

11 月 9 日，阿联酋总统外交顾问安瓦尔·加尔加什在阿布扎比战略辩论论坛上警告，中东面临长期不确定性，表示华盛顿与德黑兰达成全面政治和解的前景日益渺茫。这位阿联酋高级官员强调，地区必须为持续动荡做好准备，因为冲突后果依然难以预料。 加尔加什的评估具有分量，因为阿联酋是关键海湾国家，与华盛顿及地区各方关系密切，其外交信号往往反映海湾共识对安全威胁的看法。长期的美伊紧张局势直接威胁霍尔木兹海峡的能源流动、全球油价，以及供应全球逾 20%原油的海湾经济体稳定，进而影响中国等主要进口国。 加尔加什在周一的阿布扎比战略辩论上表示，地区应为「长期不确定性」做好准备，因为伊朗冲突的政治解决方案依然难觅。他在 2026 年 5 月曾评估美伊和平协议有「五五开」机会，但强调任何和解必须解决地区不稳定的根源。阿联酋既保持与德黑兰的外交渠道，又驻扎美军资产，定位为潜在调解者。

rss · Reuters \(English\) · 11月9日 15:01

**背景**: 阿联酋 2020 年在《亚伯拉罕协议》框架下与以色列建交，重塑海湾地缘格局，同时与波斯湾对岸邻国伊朗保持务实关系。2015 年伊核协议（JCPOA）在美方 2018 年退出后崩塌，引发油轮遇袭、伊朗导弹打击伊拉克美军基地等升级行动。作为石油输出国组织（OPEC）第三大产油国，日产约 320 万桶，阿联酋直接利益在于防止冲突扰乱霍尔木兹海峡——每日约 2100 万桶原油经此过境。

**标签**: `#Middle East`, `#Geopolitics`, `#US-Iran Relations`, `#UAE`, `#Energy Security`

---

<a id="item-25"></a>
## [孟加拉临时政府拒绝谢赫·哈西娜护照申请](https://news.google.com/rss/articles/CBMisgFBVV95cUxNQy1pMFQtX2ZjVFVyZTJSR296WXMzdl9haTFsMEk5S2RWR0wwWWpzNG12Mld0VFVIYVpnOEZnVHVBa3ppeTJVZHNjZlNyQXhxWTBDVFhiSU1nbDJUSXdlaUZzdzl5d2twLWZKMW9DazVxNFNiamQyY1h6cDM2WDUyRFM0ZjVWSTlhWWFkaWtSREtmVFVNV29qT3U3d0dBcGx1eHNBblZZQTc3ajF4Q1dQWVln?oc=5) ⭐️ 7.0/10

前孟加拉总理谢赫·哈西娜（Sheikh Hasina）自 2024 年 8 月辞职后流亡印度，她于 2026 年 11 月 9 日通过伦敦律师向孟加拉高级专员公署申请新护照和国家身份证以便回国。由穆罕默德·尤努斯（Muhammad Yunus）领导的临时政府拒绝了这一请求，路透社独家报道了这一消息。 拒绝发放护照显示尤努斯临时政府决心阻止哈西娜回国，同时孟加拉通过法律渠道向印度请求引渡，新德里表示正在审查中。哈西娜若回国可能动摇脆弱的政治过渡，并使孟印关系复杂化，印度是孟加拉的关键地区伙伴。 哈西娜曾于 1996-2001 年和 2009-2024 年两度担任总理，2024 年 8 月因大规模抗议辞职。孟加拉多次向印度请求引渡，其律师于 2026 年 11 月 9 日联系伦敦孟加拉高级专员公署。临时政府拒绝发放护照，使其在印度的法律地位悬而未决。

rss · Reuters \(English\) · 11月9日 11:27

**背景**: 谢赫·哈西娜·瓦泽德（Sheikh Hasina Wazed）主导孟加拉政治 15 年，直到 2024 年 7-8 月因就业配额引发的学生抗议演变为全国性起义，迫使她于 8 月 5 日逃往印度。由诺贝尔奖得主穆罕默德·尤努斯领导的军方支持的临时政府上台，承诺举行选举和改革。此后孟加拉对哈西娜及其盟友提起多项刑事指控，寻求印度引渡，印度以法律程序为由保持谨慎立场。

**标签**: `#Bangladesh`, `#Sheikh Hasina`, `#politics`, `#South Asia`, `#exile`

---


---

**本期模型运行状态：正常** ｜ 主通道 `nvidia/nemotron-3-ultra-550b-a55b:free` 承担 100%。

模型用量：`openai:nvidia/nemotron-3-ultra-550b-a55b:free` 1962k，`openai:deepseek-flash` 1k（合计 1962k tokens）。