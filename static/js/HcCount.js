Highcharts.chart('container3', {
    chart: {
        type: 'packedbubble',
        height: '70%'
    },
    title: {
        text: ''
    },
    tooltip: {
        useHTML: true,
        pointFormat: '<b>{point.name}:</b> {point.value} 마리'
    },
    plotOptions: {
        packedbubble: {
            minSize: '50%',
            maxSize: '500%',
            zMin: 0,
            zMax: 1000,
            layoutAlgorithm: {
                splitSeries: false,
                gravitationalConstant: 0.02
            },
            dataLabels: {
                enabled: true,
                format: '{point.name}',
                filter: {
                    property: 'y',
                    operator: '>',
                    value: 250
                },
                style: {
                    color: 'black',
                    textOutline: 'none',
                    fontWeight: 'normal'
                }
            }
        }
    },
    series: [{
        name: '대형',
        data: [{
            name: 'Afghan Hound',
            value: afghanAVGc
        },
        {
            name: 'American Pitbull Terrier',
            value: pitbullAVGc
        },
        {
            name: "Bloodhound",
            value: bloodAVGc
        },
        {
            name: "Chow Chow",
            value: chowAVGc
        },
        {
            name: "Dalmatian",
            value: dalmatianAVGc
        },
        {
            name: "Dutch Shepherd",
            value: dutchAVGc
        },
        {
            name: "English Foxhound",
            value: englishAVGc
        },
        {
            name: "German Shepherd",
            value: gershepherdAVGc
        },
        {
            name: "Goldador",
            value: goldadorAVGc
        }, {
            name: "Golden Retriever",
            value: goldenAVGc
        }, {
            name: "Great Dane",
            value: daneAVGc
        },
        {
            name: "Great Pyrenees",
            value: pyreneesAVGc
        },
        {
            name: "Greyhound",
            value: houndAVGc
        },
        {
            name: "Samoyed",
            value: samoyedAVGc
        },
        {
            name: "Siberian Husky",
            value: huskyAVGc
        },
        {
            name: "Airedale Terrier",
            value: airedaleAVGc
        },
        {
            name: "Appenzeller Sennenhund",
            value: appenzellerAVGc
        },
        {
            name: "Bulldog",
            value: bulldogAVGc
        }]
    }, {
        name: '중형',
        data: [{
            name: "American Eskimo Dog",
            value: eskimoAVGc
        },
        {
            name: "Cocker Spaniel",
            value: cockerAVGc
        },
        {
            name: "Pembroke Welsh Corgi",
            value: corgiAVGc
        },
        {
            name: "Border Collie",
            value: borderAVGc
        },
        {
            name: "German Pinscher",
            value: pinscherAVGc
        }]
    }, {
        name: '소형',
        data: [{
            name: "Australian Terrier",
            value: australianAVGc
        },
        {
            name: "Beagle",
            value: beagleAVGc
        },
        {
            name: "Bichon Frise",
            value: bichonAVGc
        },
        {
            name: "Boston Terrier",
            value: bostonAVGc
        },
        {
            name: "Chihuahua",
            value: chiAVGc
        },
        {
            name: "Dachshund",
            value: dachhundAVGc
        },
        {
            name: "Poodle",
            value: poodleAVGc
        },
        {
            name: "Pug",
            value: pugAVGc
        },
        {
            name: "Shih Tzu",
            value: tzuAVGc
        },
        {
            name: "Yorkshire Terrier",
            value: yorkAVGc
        },
        {
            name: "Maltese",
            value: malteseAVGc
        },
        {
            name: "Pomeranian",
            value: pomeAVGc
        }]
    }]
});