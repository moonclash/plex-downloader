from torrentp import TorrentDownloader

class Downloader:

    async def download_torrent(self, magnet_url, target_dir):
        downloader = TorrentDownloader(magnet_url, target_dir)
        await downloader.start_download()
