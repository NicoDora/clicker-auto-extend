import { INestApplication, Injectable } from '@nestjs/common';

@Injectable()
export class BootstrapService {
  async setStartingServer(app: INestApplication) {
    await app.listen(process.env.PORT);
  }
}
