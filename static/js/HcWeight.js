Highcharts.chart('container2', {
    chart: {
        type: 'column'
    },
    title: {
        text: ''
    },
    subtitle: {
        text: '클릭하여 모든 견종의 평균 몸무게를 확인해보세요!'
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        title: {
            text: '평균 몸무게'
        }

    },
    legend: {
        enabled: false
    },
    plotOptions: {
        series: {
            borderWidth: 0,
            dataLabels: {
                enabled: true,
                format: '{point.y:.1f}kg'
            }
        }
    },

    tooltip: {
        headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
        pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}kg</b> 평균 몸무게<br/>'
    },

    series: [
        {
            name: "크기",
            colorByPoint: true,
            data: [
                {
                    name: "대형",
                    y: bigAVGw,
                    drilldown: "대형"
                },
                {
                    name: "중형",
                    y: middleAVGw,
                    drilldown: "중형"
                },
                {
                    name: "소형",
                    y: smallAVGw,
                    drilldown: "소형"
                },
                {
                    name: mynames,
                    y: myweight,
                    drilldown: null
                }
            ]
        }
    ],
    drilldown: {
        series: [
            {
                name: "대형",
                id: "대형",
                data: [
                    [
                        "Afghan Hound",
                        afghanAVGw
                    ],
                    [
                        "American Pitbull Terrier",
                        pitbullAVGw
                    ],
                    [
                        "Bloodhound",
                        bloodAVGw
                    ],

                    [
                        "Chow Chow",
                        chowAVGw
                    ],
                    [
                        "Dalmatian",
                        dalmatianAVGw
                    ],
                    [
                        "Dutch Shepherd",
                        dutchAVGw
                    ],
                    [
                        "English Foxhound",
                        englishAVGw
                    ],
                    [
                        "German Shepherd",
                        gershepherdAVGw
                    ],
                    [
                        "Goldador",
                        goldadorAVGw
                    ],
                    [
                        "Golden Retriever",
                        goldenAVGw
                    ],
                    [
                        "Great Dane",
                        daneAVGw
                    ],
                    [
                        "Great Pyrenees",
                        pyreneesAVGw
                    ],
                    [
                        "Greyhound",
                        houndAVGw
                    ],
                    [
                        "Samoyed",
                        samoyedAVGw
                    ],
                    [
                        "Siberian Husky",
                        huskyAVGw
                    ],
                    [
                        "Airedale Terrier",
                        airedaleAVGw
                    ],
                    [
                        "Appenzeller Sennenhund",
                        appenzellerAVGw
                    ],
                    [
                        "Bulldog",
                        bulldogAVGw
                    ]
                ]
            },
            {
                name: "중형",
                id: "중형",
                data: [

                    [
                        "American Eskimo Dog",
                        eskimoAVGw
                    ],
                    [
                        "Cocker Spaniel",
                        cockerAVGw
                    ],
                    [
                        "Pembroke Welsh Corgi",
                        corgiAVGw
                    ],
                    [
                        "Border Collie",
                        borderAVGw
                    ],
                    [
                        "German Pinscher",
                        pinscherAVGw
                    ]
                ]
            },
            {
                name: "소형",
                id: "소형",
                data: [
                    [
                        "Australian Terrier",
                        australianAVGw
                    ],
                    [
                        "Beagle",
                        beagleAVGw
                    ],
                    [
                        "Bichon Frise",
                        bichonAVGw
                    ],
                    [
                        "Boston Terrier",
                        bostonAVGw
                    ],
                    [
                        "Chihuahua",
                        chiAVGw
                    ],
                    [
                        "Dachshund",
                        dachhundAVGw
                    ],
                    [
                        "Poodle",
                        poodleAVGw
                    ],
                    [
                        "Pug",
                        pugAVGw
                    ],
                    [
                        "Shih Tzu",
                        tzuAVGw
                    ],
                    [
                        "Yorkshire Terrier",
                        yorkAVGw
                    ],
                    [
                        "Maltese",
                        malteseAVGw
                    ],
                    [
                        "Pomeranian",
                        pomeAVGw
                    ]
                ]
            }
        ]
    }
});