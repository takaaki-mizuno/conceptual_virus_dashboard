(this.webpackJsonpconceptual_virus_frontend=this.webpackJsonpconceptual_virus_frontend||[]).push([[0],{29:function(e,t,n){},35:function(e,t,n){"use strict";n.r(t);var r=n(0),s=n.n(r),c=n(10),a=n.n(c),i=n(24),o=n(3),u=(n(29),n(13)),d=n(21),l=n.n(d),h=n(22);function j(){return p.apply(this,arguments)}function p(){return(p=Object(h.a)(l.a.mark((function e(){var t,n,r;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,fetch("http://localhost/api/dashboard/creatures",{method:"GET"});case 3:if(t=e.sent,console.log(t),!t.ok){e.next=17;break}return e.next=8,t.json();case 8:if(n=e.sent,!(r=null===n||void 0===n?void 0:n.creatures)){e.next=14;break}return e.abrupt("return",r);case 14:case 17:return e.abrupt("return",[]);case 15:e.next=18;break;case 18:e.next=23;break;case 20:return e.prev=20,e.t0=e.catch(0),e.abrupt("return",Promise.reject(e.t0));case 23:case"end":return e.stop()}}),e,null,[[0,20]])})))).apply(this,arguments)}var b=n(23),x=n(4),f=function(e){var t={backgroundColor:[],data:[]},n={labels:[],datasets:[]};for(var r in e.trends){n.labels.push(r);var s=Number(r.charCodeAt(0)).toString(16)+Number(r.charCodeAt(1)).toString(16)+Number(r.charCodeAt(2)).toString(16);t.backgroundColor.push("#"+s),t.data.push(e.trends[r])}return n.datasets.push(t),console.log(n),Object(x.jsx)(b.a,{type:"doughnut",data:n})},v=n(15),g=function(e){return Object(x.jsx)(v.e,{xs:4,children:Object(x.jsxs)(v.a,{className:"mb-4",style:{padding:"20px"},children:[Object(x.jsx)(v.d,{style:{padding:"20px"},children:Object(x.jsx)("h3",{children:e.ipAddress})}),Object(x.jsx)(v.b,{style:{padding:"20px"},children:Object(x.jsx)(f,{total_count:e.viruses.total_count,trends:e.viruses.trends})}),Object(x.jsx)(v.c,{style:{padding:"20px"},children:Object(x.jsxs)("p",{children:[" Total Variants: ",e.viruses.total_count]})})]})})},O=function(){var e=r.useState(),t=Object(u.a)(e,2),n=t[0],s=t[1];r.useEffect((function(){j().then((function(e){e&&s(e)}));var e=setInterval((function(){j().then((function(e){e&&s(e)})).catch((function(e){console.log(e)}))}),6e4);return function(){clearInterval(e)}}),[]);var c=[];if(n)for(var a=0;a<n.length;a++){var i=n[a];c.push(Object(x.jsx)(g,{ipAddress:i.ip_address,idString:i.id,viruses:i.viruses},i.id))}return Object(x.jsx)("div",{children:Object(x.jsx)("div",{className:"wrapper d-flex flex-column min-vh-100 bg-light",children:Object(x.jsx)("div",{className:"body flex-grow-1 px-3",children:Object(x.jsxs)(v.f,{lg:!0,style:{padding:"20px"},children:[Object(x.jsx)("h1",{className:"title",style:{padding:"20px",textAlign:"center"},children:"Conceptual Virus Dashboard"}),Object(x.jsx)(v.g,{children:c})]})})})})};var m=function(){return Object(x.jsx)(i.a,{children:Object(x.jsx)(o.c,{children:Object(x.jsx)(o.a,{path:"/",element:Object(x.jsx)(O,{})})})})},y=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,36)).then((function(t){var n=t.getCLS,r=t.getFID,s=t.getFCP,c=t.getLCP,a=t.getTTFB;n(e),r(e),s(e),c(e),a(e)}))};n(33),n(34);a.a.render(Object(x.jsx)(s.a.StrictMode,{children:Object(x.jsx)(m,{})}),document.getElementById("root")),y()}},[[35,1,2]]]);
//# sourceMappingURL=main.cb165d28.chunk.js.map