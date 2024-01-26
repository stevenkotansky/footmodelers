import os
from sydney import SydneyClient
import asyncio

# https://github.com/vsakkas/sydney.py

cookie = "SRCHHPGUSR=SRCHLANG=en&BRW=W&BRH=S&CW=1470&CH=398&SCW=1470&SCH=398&DPR=2.0&UTC=-480&DM=1&CIBV=1.1514.2&HV=1706242239&PRVCW=1470&PRVCH=745&CMUID=0A013B01BFB46E1F135F2F13BE0E6FBF; MUIDB=0A013B01BFB46E1F135F2F13BE0E6FBF; _RwBf=r=0&ilt=3&ihpd=3&ispd=0&rc=0&rb=0&gb=0&rg=200&pc=0&mtu=0&rbb=0&g=0&cid=&clo=0&v=3&l=2024-01-25T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0001-01-01T00:00:00.0000000&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2024-01-26T04:10:34.8255035+00:00&rwred=0&wls=&wlb=&wle=&ccp=&lka=0&lkt=0&aad=0&TH=; _Rwho=u=d; _SS=SID=3031FBB6452E680F26F4EFA4449469B6&R=0&RB=0&GB=0&RG=200&RP=0; BFBUSR=CMUID=0A013B01BFB46E1F135F2F13BE0E6FBF; MUID=0A013B01BFB46E1F135F2F13BE0E6FBF; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=D4D0AEECCE674B7292A145F3B950E1F0&dmnchg=1; SRCHUSR=DOB=20240126; _EDGE_S=F=1&SID=3031FBB6452E680F26F4EFA4449469B6; _EDGE_V=1"

os.environ["BING_COOKIES"] = cookie

async def main() -> None:
    async with SydneyClient() as sydney:
        response = await sydney.ask("Hi, my name is Steven", citations=True)
        print(response)
    # async with SydneyClient() as sydney:
    #     while True:
    #         prompt = input("You: ")

    #         if prompt == "!reset":
    #             await sydney.reset_conversation()
    #             continue
    #         elif prompt == "!exit":
    #             break

    #         print("Sydney: ", end="", flush=True)
    #         async for response in sydney.ask_stream(prompt):
    #             print(response, end="", flush=True)
    #         print("\n")


if __name__ == "__main__":
    asyncio.run(main())

# sydney = SydneyClient()

# async def ask_question():

#     sydney = SydneyClient(style="creative")

#     async with SydneyClient() as sydney:
#         response = await sydney.ask("When was Bing Chat released?", citations=True)
#         print(response)
#         print("test")