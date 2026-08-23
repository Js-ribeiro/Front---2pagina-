import flet as ft
from cores import Cores

def main(page: ft.Page):

    page.title = "Iconic Brazil"
    page.bgcolor = "#E4E7E8"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO

    # =========================================================
    # IMAGENS
    # =========================================================

    rio = "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=1200"

    montanha = "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=1000"

    praia = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1000"

    # =========================================================
    # FUNÇÃO DE TEXTO
    # =========================================================

    def txt(
        texto,
        tamanho=14,
        cor="#222222",
        negrito=False
    ):
        return ft.Text(
            texto,
            size=tamanho,
            color=cor,
            weight=(
                ft.FontWeight.BOLD
                if negrito
                else ft.FontWeight.NORMAL
            )
        )

    # =========================================================
    # FUNÇÃO DE IMAGEM
    # =========================================================

    def imagem(src, largura, altura):

        return ft.Image(
            src=src,
            width=largura,
            height=altura
        )

    # =========================================================
    # CABEÇALHO
    # =========================================================

    cabecalho = ft.Container(
        padding=25,

        content=ft.Row(
            controls=[

                # Logo / nome
                ft.Column(
                    controls=[

                        txt(
                            "Carregadores",
                            20,
                            Cores.PRIMARIO,
                            True
                        ),

                        txt(
                            "BRASIL",
                            9,
                            Cores.SUPERFICIE_ESCURO,
                            True
                        )
                    ],

                    spacing=0
                ),

                ft.Container(
                    expand=True
                ),

                # Busca
                ft.Container(
                    width=630,
                    height=45,
                    bgcolor="#FFFFFF",
                    border_radius=25,
                    padding=10,

                    content=ft.Row(
                        controls=[

                            ft.Icon(
                                ft.Icons.SEARCH,
                                size=20,
                                color="#000000"
                            ),

                            txt(
                                "Procure carregadores",
                                15,
                               Cores.SUPERFICIE_ESCURO,
                                True
                            ),

                            ft.Container(
                                expand=True
                            ),
                        ]
                    )
                ),

                ft.Container(
                    width=20
                ),

                # Favoritos
                ft.Container(
                    width=45,
                    height=45,
                    bgcolor="#554242",
                    border_radius=25,

                    content=ft.Icon(
                        ft.Icons.FAVORITE_BORDER,
                        size=21
                    )
                ),

                ft.Container(
                    width=10
                ),

                
                ft.CircleAvatar(
                    radius=22,
                    bgcolor="#E7A56D",

                    content=txt(
                        "V",
                        15,
                        "white",
                        True
                    )
                )
            ]
        )
    )


    # =========================================================
    # IMAGEM PRINCIPAL
    # =========================================================

    imagem_principal = ft.Container(
        height=390,
        border_radius=30,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,

        content=ft.Stack(
            controls=[
                
                ft.Container(
                    content=ft.Image(
                        src =r"C:\Users\João Pedro\Desktop\workspace\front\imagem posto.png",
                        
                    ),
                    border_radius=30,
                    clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                    width=1000,
                    height=1000
                ),

                # Escurece levemente a imagem
                ft.Container(
                    bgcolor="#33000000",
                    border_radius=30
                
                ),
        

                # Conteúdo sobre a imagem
                ft.Container(
                    padding=35,

                    content=ft.Column(
                        controls=[

                            # Botões superiores
                            ft.Row(
                                controls=[

                                    ft.Container(
                                        width=42,
                                        height=42,
                                        bgcolor="#EEEEEE",
                                        border_radius=25,

                                        content=ft.Icon(
                                            ft.Icons.ARROW_BACK,
                                            size=20
                                        )
                                    ),

                                    ft.Container(
                                        expand=True
                                    ),

                                 


                                    ft.Container(
                                        width=42,
                                        height=42,
                                        bgcolor="#EEEEEE",
                                        border_radius=25,

                                        content=ft.Icon(
                                            ft.Icons.FAVORITE_BORDER,
                                            size=19
                                        )
                                    )
                                ]
                            ),

                            ft.Container(
                                expand=True
                            ),

                            # Informações
                            txt(
                                "Localização",
                                20,
                                "#EEEEEE",
                                True
                            ),

                            txt(
                                "Av. Paulista, São Paulo",
                                40,
                                "white",
                                True
                            ),

                            ft.Row(
                                controls=[

                                    ft.Icon(
                                        ft.Icons.LOCATION_ON,
                                        color="white",
                                        size=17
                                    ),

                                    txt(
                                        "Brasil",
                                        12,
                                        "white"
                                    ),

                                    ft.Container(
                                        width=15
                                    ),

                                    ft.Icon(
                                        ft.Icons.STAR,
                                        Cores.TESTE,
                                        size=16
                                    ),

                                    txt(
                                        "5.0",
                                        12,
                                        "white",
                                        True
                                    ),

                                    txt(
                                        "067reviews",
                                        12,
                                        "white"
                                    )
                                ],

                                spacing=5
                            
                            )
                        ]
                    )
                )
            ]
        )
    )

    # =========================================================
    # INFORMAÇÕES DA VIAGEM
    # =========================================================

    informacoes = ft.Container(
        bgcolor="#FFFFFF",
        border_radius=25,
        padding=25,

        content=ft.Row(
            controls=[

                ft.Column(
                    controls=[

                        txt(
                            "EletroPosto Central",
                            23,
                            negrito=True
                        ),

                        txt(
                            "status: disponivel",
                            30,
                            negrito=True,
                            
                        )
                    ],

                    spacing=4
                ),

                ft.Container(
                    expand=True
                ),

                # Duração
                ft.Column(
                    controls=[

                        txt(
                            "horario de funcionamento ",
                            19,
                            "#999999",
                            True
                        ),

                        txt(
                            "10h às 22h",
                            17,
                            negrito=True
                        )
                    ],

                    spacing=3
                ),

                ft.Container(
                    width=30
                ),

                # Preço
                ft.Column(
                    controls=[

                        txt(
                            "Preço",
                            16,
                            "#999999",
                            True
                        ),

                        txt(
                            "R$ 10,50",
                            20,
                            negrito=True
                        )
                    ],

                    spacing=3
                ),

                ft.Container(
                    width=20
                ),

                # Botão
                ft.Container(
                    width=150,
                    height=48,
                    bgcolor="#222526",
                    border_radius=25,

                    content=ft.Row(
                        controls=[

                            ft.Container(
                                expand=True
                            ),

                            txt(
                                "IR",
                                12,
                                "white",
                                True
                            ),

                            ft.Icon(
                                ft.Icons.ARROW_FORWARD,
                                color="white",
                                size=17
                            ),

                            ft.Container(
                                expand=True
                            )
                        ]
                    )
                )
            ]
        )
    )

    # =========================================================
    # DESCRIÇÃO
    # =========================================================

    descricao = ft.Container(
        width=650,

        content=ft.Column(
            controls=[

                txt(
                    "Sobre o local",
                    21,
                    negrito=True
                ),

                txt(
                    "Localizado no coração de São Paulo, na Avenida Paulista,  "
                    "o EletroPosto Central oferece uma solução prática "
                    "e eficiente para motoristas de carros elétricos. "
                    "Atenção: O posto dispõe de poucas vagas cobertas,sujeitas à "
                    "disponibilidade no momento da chegada "
                    "Aproveite a localização privilegiada para resolver seus"
                    "compromissos enquanto o seu veículo recarrega!.",
                    15,
                    "#020202"
                ),

               
            ],

            spacing=8
        )
    )

    # =========================================================
    # ROTEIRO
    # =========================================================

    titulo_roteiro = ft.Row(
        controls=[

            txt(
                "Outros Postos de abastecimento",
                21,
                negrito=True
            ),

            ft.Container(
                expand=True
            ),

            txt(
                "Parceiros de Goodwe",
                11,
                "#777777",
                True
            )
        ]
    )

    # =========================================================
    # DAY 1
    # =========================================================

    day1 = ft.Container(
        bgcolor="#FFFFFF",
        border_radius=20,
        padding=15,

        content=ft.Column(
            controls=[

                ft.Row(
                  controls=[
                     ft.Image(
                     src=r"C:\Users\João Pedro\Desktop\workspace\front\posto2.jpeg",
                     width=90,
                     height=70,
                     fit=ft.BoxFit.CONTAIN,  # Opcional: ajusta como a imagem se comporta no espaço
                    ),

                        ft.Container(
                            width=15
                        ),

                        ft.Column(
                            controls=[

                                txt(
                                    "Zona Norte, São Paulo",
                                    9,
                                    "#999999",
                                    True
                                ),

                                txt(
                                    "VoltPark Norte",
                                    15,
                                    negrito=True
                                ),

                                txt(
                                    "disponivel",
                                    10,
                                    "#777777"
                                )
                            ],

                            spacing=4
                        ),

                        ft.Container(
                            expand=True
                        ),

                        ft.Icon(
                            ft.Icons.KEYBOARD_ARROW_UP,
                            size=22
                        )
                    ]
                ),

                ft.Divider(
                    height=10,
                    color="#EEEEEE"
                ),

                txt(
                    "Preço",
                    10,
                    "#999999",
                    True
                ),

                txt(
                    "R$ 1,35/kWh"
                    ,
                    11
                ),

                txt(
                    "Numero de vagas",
                    10,
                    "#999999",
                    True
                ),

                txt(
                    "3",
                    11
                ),


            ],

            spacing=7
        )
    )



    # =========================================================
    # PAINEL LATERAL
    # =========================================================

    painel_lateral = ft.Container(
        width=320,
        bgcolor="#FFFFFF",
        border_radius=25,
        padding=22,

        content=ft.Column(
            controls=[

                txt(
                    "Detalhes",
                    19,
                    negrito=True
                ),

                ft.Divider(
                    color="#EEEEEE"
                ),

                ft.Row(
                    controls=[

                        ft.Icon(
                            ft.Icons.CALENDAR_MONTH,
                            size=20
                        ),

                        ft.Column(
                            controls=[

                                txt(
                                    "fluxo de pessoas",
                                    9,
                                    "#999999"
                                ),

                                txt(
                                    "Alta",
                                    12,
                                    negrito=True
                                )
                            ],

                            spacing=2
                        )
                    ]
                ),

                ft.Row(
                    controls=[

                        ft.Icon(
                            ft.Icons.GROUP,
                            size=20
                        ),

                        ft.Column(
                            controls=[

                                txt(
                                    "O local oferece uma ampla variedade de opções e serviços",
                                    9,
                                    "#999999"
                                ),

                                txt(
                                    "30 estabelecimentos pareceiros",
                                    12,
                                    negrito=True
                                )
                            ],

                            spacing=2
                        )
                    ]
                ),

                ft.Row(
                    controls=[

                        ft.Icon(
                            ft.Icons.LANGUAGE,
                            size=20
                        ),

                        ft.Column(
                            controls=[

                                txt(
                                    "Numero de carregadores",
                                    9,
                                    "#999999"
                                ),

                                txt(
                                    "5",
                                    12,
                                    negrito=True
                                )
                            ],

                            spacing=2
                        )
                    ]
                ),

                ft.Container(
                    height=10
                ),

                ft.Container(
                    bgcolor="#F1F3F3",
                    border_radius=18,
                    padding=15,

                    content=ft.Column(
                        controls=[

                            txt(
                                "vantagens exclusivas aplicáveis aos clientes assinantes",
                                14,
                                negrito=True
                            ),

                            txt(
                                "✓ Reservar a vaga com antecedência",
                                10,
                                "#666666"
                            ),

                            txt(
                                "✓ Cashback",
                                10,
                                "#666666"
                            ),

                        
                        ],

                        spacing=7
                    )
                ),

                ft.Container(
                    expand=True
                ),

                # Botão principal
                ft.Container(
                    height=55,
                    bgcolor="#222526",
                    border_radius=28,

                    content=ft.Row(
                        controls=[

                            ft.Container(
                                expand=True
                            ),

                            txt(
                                "Se deslocar ",
                                20,
                                "white",
                                True
                            ),

                            ft.Icon(
                                ft.Icons.ARROW_FORWARD,
                                color="white",
                                size=18
                            ),

                            ft.Container(
                                expand=True
                            )
                        ]
                    )
                )
            ],

            spacing=15
        )
    )

    # =========================================================
    # CONTEÚDO PRINCIPAL
    # =========================================================

    conteudo = ft.Container(
        width=1100,

        content=ft.Column(
            controls=[

                cabecalho,

                imagem_principal,

                informacoes,

                ft.Row(
                    controls=[

                        ft.Column(
                            controls=[

                                descricao,

                                ft.Container(
                                    height=20
                                ),

                                titulo_roteiro,

                                day1,

                                

                            
                            ],

                            spacing=15,

                            expand=True
                        ),

                        painel_lateral
                    ],

                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=25
                )
            ],

            spacing=20
        )
    )

    # =========================================================
    # ADICIONAR NA PÁGINA
    # =========================================================

    page.add(
        ft.Container(
            width=1200,
            padding=20,
            content=conteudo
        )
    )


ft.app(target=main)