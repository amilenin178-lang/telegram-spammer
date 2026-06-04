from telethon import TelegramClient
import asyncio

API_ID = 30151741
API_HASH = '4be312d31687c3802db8260198ac3f26'
PHONE_NUMBER = '+573171714738'

# ВСЕ 145 ЧАТОВ (полный список)
CHATS = [
    'ukradi_breinrota10',
    'Steal_a_Brainrotq',
    'standoff_pubg_chat',
    'Steal_a_BrainrotGG',
    'prodatgoldstandoff2',
    'kupiprodaiso2so',
    'delay_vz_zdes',
    'steal_a_brainrotac',
    'steal_a_brainrotag',
    'pabg_pubgg',
    'StealABrainrotTrade',
    'steal_a_brainrottl',
    'brawlstarschatpiar',
    'poisktimi_brawl',
    'NFT_Chat_1',
    'stendoff_pabgi',
    'Pubg_chatiks',
    'brawlstars_findteam',
    'paeserrr_otc',
    'Steal_a_Brainrotaa',
    'pubg_pabga',
    'ChatzBrawlStars',
    'Steal_A_Brainrota21',
    'chat_manerki',
    'NFT_chat_chat',
    'reck_uslugi',
    'chatpubg58',
    'Bear_Chatik',
    'czzo0_chat',
    'GrandMobail_Chats',
    'nftchatSeller',
    'NFT_Chatcik',
    'Detroitafk',
    'NFT_NFT_NFT_NFT12',
    'chatus_nft',
    'chat2_manerki',
    'matizokso2_reviews',
    'Dis_uslugi',
    'taigerchatik',
    'nft_sellers_chats',
    'nft_chat_use',
    'chat3_manerka',
    'TradeZoneNFT',
    'nft_chatzx',
    'shatprodat',
    'poisk_chats',
    'stars_chat_brawll',
    'chat5_manerka',
    'reck_uslg_v2',
    'controlchatobnl',
    'BrawlStarsChat97',
    'brawlstasrschat',
    'GusFringChatt',
    'vzchat1ik',
    'chatpubg22O',
    'Steal_a_Brainrota',
    'Steal_a_brainrotikq',
    'GRAND_CHATIX',
    'standoff_pabg_chat',
    'chat_stars_brawl',
    'StealABrainrotRu',
    'HavunSellChat',
    'steaI_a_brainroth',
    'chatstandoff220',
    'Nft_Chaton',
    'TakeABrain',
    'NFT300000',
    'MonsterEnergy_USLUGY',
    'Steal_A_Brainrota0',
    'snark_pbc',
    'Formscham',
    'brawllchatik',
    'brainrota_a_steal',
    'TrapUSLUG',
    'akatsuke_chat',
    'AMIRINchat',
    'TrapUslug2',
    'bravl_chat_stars',
    'chatik_zv',
    'HavunNFTchat',
    'millionsgift',
    'trolling029',
    'search_chatbs',
    'gormon_rosta4',
    'TonziChat',
    'raidchats99',
    'salersboard',
    'HavunDesign',
    'chat_nft_uslugi',
    'nfchat12',
    'VZ2752',
    'truegarantshop',
    'HavunSellChat1',
    'BarbarisTradeChat',
    'wsteal_a_brainrot',
    'steal_a_brainrota20',
    'ykrady_brainrota_chat',
    'shopppp3',
    'javatreys',
    'nft_chatif',
    'skypworkerr',
    'pabg_pubgg',
    'steal_a_brainrotay',
    'steal_a_brainrota01',
    'Roblox302',
    'buysellchat_tg',
    'chat_mlorin2',
    'cemlle',
    'Iegit_chat',
    'MonkeyMarketTop',
    'DamaskNFT',
    'piar_chat404',
    'chatbravlikbs',
    'doxchattroll',
    'Ayanokojigarant_chat',
    'Chatik4ss',
    'racc4lka4',
    'alnexts_tgk',
    'starrr_void',
    'elbrus_chatik',
    'Bsbrawlchatw',
    'hexuspiar',
    'vz_sovmi_megi_papki',
    'CHAT_PUBG1_METRO',
    'nftgiftsprodaza',
    'stealabraichat',
    'chatemirate',
    'Steal_a_brainrotscha',
    'zuda_chat1',
    'brawlstarsfire',
    'poisk_bs_chatiks',
    'neiron_chat2',
    'HAVUNCHAT',
    'sweetnft19',
    'HavunSellChat2',
    'Chatuslug09',
    'nfti_chatik',
    'Chatikc_nft',
    'BOND_CHATIX',
    'roblox_tradechat_chat',
    'drop_cht',
    'Mossy4kaNFT',
    'RichBazaChat',
    'chat_brawl3',
    'PlayerokkChatFunpay'
]

TEXT = "ЛУЧШИЕ ФИЗЫ ПО 20₽ В @Shopzxfizbot"
PAUSE = 60  # секунд между циклами

client = TelegramClient('account_colombia', API_ID, API_HASH)

async def main():
    await client.start(phone=PHONE_NUMBER)
    me = await client.get_me()
    print(f"✅ Запущено: {me.first_name}")
    print(f"📋 Всего чатов: {len(CHATS)}")
    
    цикл = 0
    while True:
        цикл += 1
        print(f"\n[{__import__('datetime').datetime.now().strftime('%H:%M:%S')}] 🔁 ЦИКЛ {цикл}")
        
        for чат in CHATS:
            try:
                await client.send_message(чат, TEXT)
                print(f"   ✅ {чат}")
            except Exception as e:
                print(f"   ❌ {чат}: {str(e)[:50]}")
        
        await asyncio.sleep(PAUSE)

with client:
    client.loop.run_until_complete(main())
