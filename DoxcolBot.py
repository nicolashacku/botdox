import requests
import os
import json
import discord
from discord.ext import commands
request = requests.get("https://pastebin.com/raw/rtHLA0wt")
a = request.text
key = a
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>',intents=intents)
@bot.command(case_insensitive=True)
async def nombres(ctx, tipo=None, numero=None):
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    else:
        url = f"https://api.verifik.co/v2/co/cedula?documentType={tipo}&documentNumber={numero}"
        payload={}
        headers = {
        'Authorization': f'JWT {key}'
        }   
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            fullName = j['data']['fullName']
            firstName = j['data']['firstName']
            lastName = j['data']['lastName']
            embed = discord.Embed(
                colour = discord.Colour.blue()
                
            )
            embed.add_field(name=f'Nombre Completo', value =f'{fullName}',inline=False)
            embed.add_field(name=f'Nombres', value =f'{firstName}',inline=True)
            embed.add_field(name=f'Apellido', value =f'{lastName}',inline=True)
            embed.set_footer(text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)
    
@bot.command(case_insensitive=True)
async def vehiculo(ctx, tipo=None, numero=None, placa=None):
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE, TI, PA, RC")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    elif placa == None:
        await ctx.send("Debe digitar la placa del vehiculo XXXXXX")
    else:
        url = f"https://api.verifik.co/v2/co/runt/vehiculo?documentType={tipo}&documentNumber={numero}&plate={placa}"
        payload={}
        headers = {
        'Authorization': f'JWT {key}'
        }   
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            placa = j['data']['plate']
            color = j['data']['vehicleInformation']['color']
            marca = j['data']['vehicleInformation']['brand']
            activacion = j['data']['vehicleInformation']['enrollmentDate']
            status = j['data']['vehicleInformation']['status']
            numeroSoat = j['data']['soat']['soatNumber']
            expedicionSoat = j['data']['soat']['expeditionDate']
            vecimientoSoat = j['data']['soat']['dueDate']
            tecnomecanica = j['data']['techReview']['valid']
            numeroTecno = j['data']['techReview']['reviewNumber']
            expedicionTecno = j['data']['techReview']['valid']
            vencimientoTecno = j['data']['techReview']['dueDate']
            response2 = requests.get(f"https://api.verifik.co/v2/co/runt/vehiculo-completo?plate={placa}")
            #j2 = response2.json()
            #tipoServicio = j2['data']['vehicle']['tipoServicio']
            ##numMotor = j2['data']['vehicle']['noMotor']
            #numChasis = j2['data']['vehicle']['noChasis']
            #cilindraje = j2['data']['vehicle']['1000']
            #ocupantes = j2['data']['vehicle']['ocupantes']
            
            embed = discord.Embed(
                colour = discord.Colour.blue()
                
            )
            embed.add_field(name=f'placa', value =f'{placa}',inline=False)
            embed.add_field(name=f'color', value =f'{color}',inline=True)
            embed.add_field(name=f'marca', value =f'{marca}',inline=True)
            embed.add_field(name=f'activacion', value =f'{activacion}',inline=True)
            embed.add_field(name=f'status', value =f'{status}',inline=True)
            embed.add_field(name=f'numero SOAT', value =f'{numeroSoat}',inline=True)
            embed.add_field(name=f'Expedicion Soat', value =f'{expedicionSoat}',inline=True)
            embed.add_field(name=f'Vencimiento Soat', value =f'{vecimientoSoat}',inline=True)
            embed.add_field(name=f'Tecnomecanica', value =f'{tecnomecanica}',inline=True)
            embed.add_field(name=f'Numero Tecnomecanica', value =f'{numeroTecno}',inline=True)
            embed.add_field(name=f'Expedicion Tecno', value =f'{expedicionTecno}',inline=True)
            embed.add_field(name=f'Vencimiento Tecno', value =f'{vencimientoTecno}',inline=True)
            #embed.add_field(name=f'Tipo Servicio', value =f'{tipoServicio}',inline=True)
            #embed.add_field(name=f'Numero Motor', value =f'{numMotor}',inline=True)
            #embed.add_field(name=f'Numero chasis', value =f'{numChasis}',inline=True)
            #embed.add_field(name=f'Cilindraje', value =f'{cilindraje}',inline=True)
            #embed.add_field(name=f'Limite ocupantes', value =f'{ocupantes}',inline=True)
            embed.set_footer(text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)
    
@bot.command()
async def conductor(ctx, tipo=None, numero=None):
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, CE")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    else:
        url = f"https://api.verifik.co/v2/co/runt/consultarConductor?documentType={tipo}&documentNumber={numero}"
        payload={}
        headers = {
        'Authorization': f'JWT {key}'
        }   
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            fullName = j['data']['fullName']
            totalLicencias = j['data']['totallicencias']
            #numeroLicencia = j['data']['licencias']['licenceNumber']
            #statusLicencias = j['data']['licencias']['status']
            #vencimientoLicencia = j['data']['licencias']['dueDate']
            pazandSafe = j['data']['transitTaxes']['paceAndSafe']
            pazNumber = j['data']['transitTaxes']['paceAndSafeNumber']
            transitTaxesNumber = j['data']['transitTaxes']['transitTaxesNumber']
            suspensiones = j['data']['transitTaxes']['suspensionDate']
    
            embed = discord.Embed (
                colour = discord.Colour.blue()
                
            )
            embed.add_field(name=f'Nombre Completo', value =f'{fullName}',inline=False)
            embed.add_field(name=f'Total de licencias', value =f'{totalLicencias}',inline=True)
            #embed.add_field(name=f'Numero licencia', value =f'{numeroLicencia}',inline=True)
            #embed.add_field(name=f'Estado licencia', value =f'{statusLicencias}',inline=True)
            #embed.add_field(name=f'Vencimiento licencia', value =f'{vencimientoLicencia}',inline=True)
            embed.add_field(name=f'Paz y Salvo', value =f'{pazandSafe}',inline=True)
            embed.add_field(name=f'Numero paz y salvo', value =f'{pazNumber}',inline=True)
            embed.add_field(name=f'Numero de impuestos', value =f'{transitTaxesNumber}',inline=True)
            embed.add_field(name=f'Numero de suspensiones', value =f'{suspensiones}',inline=True)
            embed.set_footer(text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)

@bot.command()
async def afiliaciones(ctx,tipo=None,numero=None,fecha=None):
    if tipo == None:
        await ctx.send("Debe un tipo de documento CC, PA, CE, PEP, TI.")
    elif numero == None:
        await ctx.send("Debe digitar un numero de identifiacion")
    elif fecha == None:
        await ctx.send("Debe digitar una fecha de nacimiento")
    else:
        url = f"https://api.verifik.co/v2/co/afiliaciones?documentType={tipo}&documentNumber={numero}&date={fecha}"
        payload={}
        headers = {
        'Authorization': f'JWT {key}'
        }   
        response = requests.get(url, headers=headers, data=payload)
        if response.status_code != 200:
            await ctx.send("Ha ocurrido un error o proporcionaste informacion incorrecta.")
        else:
            j = response.json()
            fechaCorte = j['data']['informacionPersonal']['fechaCorte']
            primerNombre = j['data']['informacionPersonal']['primerNombre']
            segundoNombre = j['data']['informacionPersonal']['segundoNombre']
            primerApellido = j['data']['informacionPersonal']['primerApellido']
            segundoApellido = j['data']['informacionPersonal']['segundoApellido']
            sexo = j['data']['informacionPersonal']['sexo']
            eps = j['data']['eps']['eps']
            regimen = j['data']['eps']['regimen']
            fechaAfiliacion = j['data']['eps']['fechaAfiliacion']
            estadoAfiliacion = j['data']['eps']['estadoAfiliacion']
            fechaAfiliacion = j['data']['eps']['fechaAfiliacion']
            tipoAfiliado = j['data']['eps']['tipoAfiliado']
            embed = discord.Embed (
                colour = discord.Colour.blue()
                
            )
            embed.add_field(name=f'Fecha corte', value =f'{fechaCorte}',inline=False)
            embed.add_field(name=f'Primer nombre', value =f'{primerNombre}',inline=True)
            embed.add_field(name=f'Segundo Nombre', value =f'{segundoNombre}',inline=True)
            embed.add_field(name=f'Primer apellido', value =f'{primerApellido}',inline=True)
            embed.add_field(name=f'Segundo apellido', value =f'{segundoApellido}',inline=True)
            embed.add_field(name=f'sexo', value =f'{sexo}',inline=False)
            embed.add_field(name=f'Eps', value =f'{eps}',inline=True)
            embed.add_field(name=f'Regimen', value =f'{regimen}',inline=True)
            embed.add_field(name=f'Fecha afiliacion', value =f'{fechaAfiliacion}',inline=False)
            embed.add_field(name=f'Estado afiliacion', value =f'{estadoAfiliacion}',inline=False)
            embed.add_field(name=f'Fecha afiliacion', value =f'{fechaAfiliacion}',inline=True)
            embed.add_field(name=f'Tipo Afiliado', value =f'{tipoAfiliado}',inline=True)
            embed.set_footer(text='Desarrollado por https://instagram.com/nicolas.5301')
            await ctx.send(embed=embed)

@bot.command()
async def comandos(ctx):
    embed = discord.Embed (
    title='DoxColBot',
    description='Desarrolado por nicolas.5301\n https://instagram.com/nicolas.5301',
    colour = discord.Colour.blue()
            
    )
    embed.add_field(name='>nombres',value='Consulta el nombre por su CC, CE', inline=False)
    embed.add_field(name='>vehiculo',value='Da toda la informacion del vehiculo con el numero de documento y placa',inline=False)
    embed.add_field(name='>conductor',value='nombres del conductor por CC, CE',inline=False)
    embed.add_field(name='>afiliaciones',value='Consulta eps y afliaciones, uso >afilaciones tipo_doc numero_doc fecha_nacmiento',inline=False)

    await ctx.send(embed=embed)
    
@bot.command()
async def borrar(ctx):
    await ctx.channel.purge(limit=None)


bot.run(os.environ['DISCORD_TOKEN'])