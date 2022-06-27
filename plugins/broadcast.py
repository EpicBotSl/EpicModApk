@Client.on_message(filters.incoming & filters.chat(-1001645439750))
async def bchanl(bot, update, broadcast_ids={}): 
    all_users = await database.get_all_users()
    broadcast_msg= update
    while True:
        broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
        if not broadcast_ids.get(broadcast_id):
            break

    out = await bot.send_message(-1001689365631,f"Ads Broadcast Started! You will be notified with log file when all the users are notified.")
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(total = total_users, current = done, failed = failed, success = success)
        
    async with aiofiles.open('broadcastlog.txt', 'w') as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id = int(user['id']), message = broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await database.delete_user(user['id'])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(dict(current = done, failed = failed, success = success))
        
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    
    completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
    await asyncio.sleep(3)
    await out.delete()
    
    if failed == 0:
        await bot.send_message(-1001689365631, f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
    else:
        await bot.send_document(-1001689365631, 'broadcastlog.txt', caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
    os.remove('broadcastlog.txt') 
    
        
