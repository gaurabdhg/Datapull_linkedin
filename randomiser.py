
def rndm():
    import time
    import random

    e='55955277349071783793421637012050054513263835440001863239914907054797780566978533580489669062951194324730995876552368128590413832411607226029983305353708761389396391779574540161372236187893652605381558415871869255386061647798340254351284396129460352913325942794904337299085731580290958631382683291477116396337092400316894586360606458459251269946557248391865642097526850823075442545993769170419777800853627309417101634349076964237222943523661255725088147792231519747780605696725380171807763603462459278778465850656050780844211529697521890874019660906651803516501792508868331483280270655383300469329011574414756313999722170380461709289457909627166226074071874997535921275608441473782330327033016823719364800217328573493594756433412994302485023573221459784328264142168487872167336701061509424345698440187331281010794512722373788612605816566805371439612788873252737389039289050686532413806279602593038772769778379286840932536588073398845721874602100531148335132385004782716937621800490479559795929059165547050577751430817511269898518840871856402603530558373783242292418562564425502267215598027401261797192804713960068916382866527700975276706977703643926022437284184088325184877047263844037953016690546593746161932384036389313136432713768884102681121989127522305625675625470172508634976536728860596675274086862740791285657699631378975303466061666980421826772456053066077389962421834085988207186468262321508028828635974683965435885695213533732531666345466588597286659'
    pi='4539057962685610055081066587969981635747363840525714591028970641401109712062804390397595156771577004203378699360072305587631421874712053292819182618612586732157919841484882916447060957527069572209175671167229109816909152801735067127485832228718352093539657251210835791513698820914442100675103346711031412671113699086585163983150197016515116851714376576183515565088490998985998238734552833163550764791853589322618548963213293308985706420467525907091548141654985946163718027098199430992448895757128289059232332609729971208443357326548938239119325974636673058360414281388303203824903758985243744170291327656180937734440307074692112019130203303801976211011004492932151608424448596376698389522868478312355265821314495768572624334418930396864262434107732269780189151044682325271620105221116603966655730925471105578537634668206531098965269186205647693125705863566201855810072936065987648611791045334885034611365768675324944166803962657978771855608455296541266540853014344431858676975145661406800700237877659134401712749470420562230538994561314071127000407854733269939081454664645880797270826683063432858785698305235808933065757406795457163775254202114955761581400250126228594130215097925923099079654737612551765675135751782966645477917450112996148903046399471329621073404375189573596145890193897131117904297828564750320319869151402870808599048010941214722131794764777262241425485454033215718530614228813758504306332175182979866223717215916077166925474873898665494945'


    randval=random.randint(5,1450)

    if (randval%2==0):
        sleeptime=int(pi[randval:(randval+1)])

    else:
        sleeptime=int(e[randval:(randval+1)])

    
    if (sleeptime<10):
        sleeptime += 12


    
    time.sleep(sleeptime)
    
    return