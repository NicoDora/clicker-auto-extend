import { INestApplication, Injectable } from '@nestjs/common';
import { config } from 'dotenv';

config();

@Injectable()
export class BootstrapService {
  async setStartingServer(app: INestApplication) {
    await app.listen(process.env.PORT);
  }
}
